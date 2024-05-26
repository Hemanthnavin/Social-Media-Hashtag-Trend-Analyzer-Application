# Social-Media-Hashtag-Trend-Analyzer-Application


**Technologies**
Python, SQL , AWS Lambda , Dynamodb,  Streamlit

**Problem Statement:**
In the era of social media dominance, users crave platforms that offer seamless posting experiences while also providing insights into trending topics. To address this need, we aim to develop a Streamlit application that allows users to compose and publish posts, same as popular social media platforms. This application will integrate with AWS Lambda and DynamoDB to facilitate post processing and hashtag analysis.

**Features:**
Post Composition: Users can write posts containing text and hashtags using the provided interface.
Post Submission: Upon clicking the "Post" button, the application will trigger a backend process sending the post content to AWS Lambda.
AWS Lambda Integration: AWS Lambda will receive the post content and parse it, extracting hashtags and post text. It will then store this data in DynamoDB.
Trending Hashtags: Users can view trending hashtags by clicking the "Show Trending Hashtags" button. This action triggers an analysis of the DynamoDB table to aggregate and identify popular hashtags.
Dynamic Updates: The trending hashtags section will dynamically update as new posts are made and analyzed, providing real-time insights into trending topics.
User Interface: The application will have an intuitive and user-friendly interface, making it easy for users to compose posts and explore trending hashtags.

**Problem Scope:**
Develop a Streamlit application that enables users to compose and publish posts containing text and hashtags.
Integrate the application with AWS Lambda to process posts and store data in DynamoDB.
Implement functionality to analyze the DynamoDB table and identify trending hashtags.
Ensure real-time updates of trending hashtags as new posts are submitted.

**Success Criteria:**
Users can compose and publish posts using the application.
Posts are processed by AWS Lambda and stored in DynamoDB, maintaining the integrity of the post text and hashtags.
The application accurately identifies and displays trending hashtags based on analysis of the DynamoDB table.
Trending hashtags update dynamically as new posts are made, ensuring real-time insights for users.
