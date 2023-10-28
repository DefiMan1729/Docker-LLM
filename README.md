# Exposing LLM/GenAI based services as API 

This is a FastAPI application that uses the LangChain library and OpenAI to analyze employee feedback.

## Overview

The application uses the OpenAI API to generate language models, which are then used to analyze the feedback. The analysis involves three steps:

1. Summarizing the feedback.
2. Identifying the employee's weaknesses.
3. Providing an improvement plan based on the identified weaknesses.

The application is available via the following endpoint

## Usage

The application provides three endpoints:
- `/feedback/{feedback}`: Takes a string of feedback as input and returns a summary of the feedback, identified weaknesses, and a recommended improvement plan.

## Example

Here's how you can use the feedback endpoint:

```bash
curl -X GET "http://localhost:8000/feedback/{feedback}"
```
Replace `{feedback}` with the actual feedback string. The response will be a JSON object containing the summary, weaknesses, and recommendation.
