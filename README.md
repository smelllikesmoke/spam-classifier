# spam-classifier

The project is made using a model from sk-learn and streamlit for the front-end. 

To run the project, you can do it directly from streamlit or using Docker.

## Through Streamlit
Before this make sure all of your dependencies are installed.
`pip3 install -r requirements.txt`

Once this is done, run the streamlit app using:

`streamlit run app.py`

## Docker
Make sure Docker is installed on your OS and it's Daemon is running.

To build the image:
`sudo docker build -t email-classifier:latest .`

To run the container:
`sudo docker run -p 8501:8501 email-classifier`

We must expose the 8501 port as that is used by streamlit. 

The size of the image would be around 1.2gbs.

Enjoy!!!
