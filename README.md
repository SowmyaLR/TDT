# TDT

Steps to run TDT app

1. Clone this repository
2. Navigate to src - <b> cd src </b>
3. Install the requirements - <b> pip install -r requirements.txt </b>
4. Update .env file for the following variables by replacing ***
    <ul>
        <li>ENDPOINT=cosmosdb_host</li>
        <li>DATABASE=database_name_used_in_cosmosdb</li>
        <li>COLLECTION=collection_name_used_in_cosmosdb</li>
        <li>PRIMARY_KEY=primary_key_of_cosmosdb</li>
        <li>BUCKET_NAME=cloud_public_bucket_name</li>
        <li>FOLDER_NAME=bucket_folder_name</li>      
    </ul>
5. Run the command - <b> python3 main.py </b>
6. Navigate to http://127.0.0.1:5000/sync in browser. once the data sync is completed <b>Data sync completed</b> will be displayed
