# TDT

Steps to run TDT app

1. Clone this repository
2. Navigate to src - <b> cd src </b>
3. Install the requirements - <b> pip install -r requirements.txt </b>
4. Create .env file and add the following env variables
    <ul>
        <li>ENDPOINT</li>
        <li>DATABASE</li>
        <li>COLLECTION</li>
        <li>PRIMARY_KEY</li>
        <li>BUCKET_NAME</li>
        <li>FOLDER_NAME</li>
        <li>DESTINATION_FOLDER=graph_data</li>
    </ul>
5. Run the command - <b> python3 main.py </b>
6. Navigate to http://127.0.0.1:5000/sync in browser. once the data sync is completed <b>Data sync completed</b> will be displayed
