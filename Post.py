import streamlit as st
import boto3
import json

# AWS Configuration
AWS_REGION = "ap-south-1"
LAMBDA_POST_FUNCTION = "ProcessPost"
LAMBDA_TRENDING_FUNCTION = "AnalyzeTrendingHashtags"

# Initialize the boto3 client for Lambda
lambda_client = boto3.client('lambda', region_name=AWS_REGION)

def main():
    st.title("Post Composer")

    # Text input for composing the post
    post_text = st.text_area("Compose your post", height=200)

    # Character count
    remaining_chars = 280 - len(post_text)
    st.write(f"Characters remaining: {remaining_chars}")

    # Hashtag input
    hashtags = st.text_input("Add hashtags (comma-separated)")

    # Splitting hashtags by comma and stripping extra spaces
    hashtags_list = [tag.strip() for tag in hashtags.split(',') if tag.strip()]

    # Displaying selected hashtags
    if hashtags_list:
        st.write("Selected Hashtags:", ", ".join([f"#{tag}" for tag in hashtags_list]))

    # Button to publish the post
    if st.button("Publish"):
        if len(post_text) > 280:
            st.error("Post exceeds 280 characters!")
        else:
            response = publish_post(post_text, hashtags_list)
            if response and response.get('statusCode') == 200:
                st.success("Post published successfully!")
            else:
                st.error("Failed to publish post.")
                if response:
                    st.write(f"Error: {response.get('statusCode')}, {response.get('body')}")

    # Button to fetch and display trending hashtags
    if st.button("Show Trending Hashtags"):
        trending_hashtags = fetch_trending_hashtags()
        if trending_hashtags:
            st.write("Trending Hashtags:")
            for hashtag in trending_hashtags:
                st.write(f"- #{hashtag}")
        else:
            st.error("Failed to fetch trending hashtags.")

def publish_post(text, hashtags):
    payload = {
        "post_text": text,
        "hashtags": hashtags
    }

    try:
        response = lambda_client.invoke(
            FunctionName=LAMBDA_POST_FUNCTION,
            InvocationType='RequestResponse',
            Payload=json.dumps(payload)
        )
        response_payload = json.loads(response['Payload'].read().decode('utf-8'))
        return response_payload
    except Exception as e:
        st.error(f"Request failed: {e}")
        return None

def fetch_trending_hashtags():
    try:
        response = lambda_client.invoke(
            FunctionName=LAMBDA_TRENDING_FUNCTION,
            InvocationType='RequestResponse'
        )
        response_payload = json.loads(response['Payload'].read().decode('utf-8'))
        if response_payload.get('statusCode') == 200:
            trending_hashtags = json.loads(response_payload.get('body', '[]'))
            return trending_hashtags
        else:
            st.error(f"Error: {response_payload.get('statusCode')}, {response_payload.get('body')}")
            return None
    except Exception as e:
        st.error(f"Request failed: {e}")
        return None

if __name__ == "__main__":
    main()
