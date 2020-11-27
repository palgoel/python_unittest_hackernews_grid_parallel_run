FROM python:3

# set a directory for the app
WORKDIR /usr/src/app
# copy all the files to the container
COPY . .
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# tell the port number the container should expose
# run the command
EXPOSE 4444
CMD ["python" , "./test_grid.py"]