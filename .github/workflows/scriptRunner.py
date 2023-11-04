name: Run Script Daily

on:
  schedule:
    - cron: '30 3 * * *' # Schedule the workflow to run at 9 AM IST every day (9:00 AM IST is 3:30 AM UTC)

jobs:
  run-script:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.x

    - name: Install dependencies
      run: pip install praw

    - name: Run Script
      run: python src/redditechobot.py
      env:
        CLIENT_ID: ${{ secrets.CLIENT_ID }}
        CLIENT_SECRET: ${{ secrets.CLIENT_SECRET }}
        USER_AGENT: ${{ secrets.USER_AGENT }}
        REDDIT_USERNAME: ${{ secrets.REDDIT_USERNAME }}
        REDDIT_PASSWORD: ${{ secrets.REDDIT_PASSWORD }}
