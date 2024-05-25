<h1>FastAPI Webhook and Polling</h1>

<p>This project implements webhook and polling endpoints using FastAPI to upload PDF files, process them, and check their processing status.</p>

<h2>Installation</h2>

<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/Sweta-Raj31/FastApi.git
cd FastApi
</code></pre></li>
  <li>Install the dependencies:
    <pre><code>pip install -r requirements.txt
</code></pre></li>
</ol>
<h1>Installing Redis on Windows</h1>

<p>For Windows, you can use the official Redis for Windows maintained by Microsoft Open Tech.</p>

<h2>Download Redis for Windows:</h2>

<ol>
  <li>Go to the <a href="https://github.com/microsoftarchive/redis/releases">Microsoft Archive</a> and download the latest Redis .zip file.</li>
</ol>

<h2>Extract the Redis files:</h2>

<ol start="2">
  <li>Extract the contents of the .zip file to a location of your choice.</li>
</ol>

<h2>Run Redis:</h2>

<ol start="3">
  <li>Open Command Prompt and navigate to the folder where you extracted Redis.</li>
  <li>Run the Redis server:
    <pre><code>redis-server.exe</code></pre>
  </li>
</ol>

<h2>Check if Redis is running:</h2>

<ol start="5">
  <li>Open another Command Prompt window and run:
    <pre><code>redis-cli.exe ping</code></pre>
  </li>
  <li>You should see a response: <strong>PONG</strong>.</li>
</ol>
<h2>Usage</h2>
<h3>Running the Application</h3>

<h2>Running Celery</h2>

<p>Celery is used for asynchronous task processing. To start Celery, open a new terminal and navigate to the project directory.</p>

<ol>
  <li>Start a Celery worker:
    <pre><code>celery -A app.celery:celery_app worker --loglevel=info
</code></pre></li>
  
</ol>
<h2>Running uvicorn</h2>
<p>To run the FastAPI application, execute the following command:</p>

<pre><code>uvicorn app.main:app --reload
</code></pre>

<p>This will start the FastAPI server locally.</p>
<li><strong>http://127.0.0.1:8000/docs#/</strong><code></code></li>



<h3>Webhook Endpoint</h3>

<h4>Description:</h4>

<p>This endpoint allows you to upload a PDF file, which will be processed and the extracted text data will be sent to a specified webhook URL.</p>

<ul>
  <li><strong>http://127.0.0.1:8000/docs#/default/upload_pdf_webhook__post</strong> <code></code></li>
  <li><strong>Method:</strong> POST</li>
  <li><strong>Request Body:</strong>
    <ul>
      <li><code>file</code>: The PDF file to be uploaded.</li>
    </ul>
  </li>
  <li><strong>Response:</strong>
    <ul>
      <li><code>pdf_id</code>: Unique identifier for the uploaded PDF.</li>
      <li><code>text</code>: Extracted text data from the PDF.</li>
    </ul>
  </li>
</ul>




<p>This endpoint allows you to check the processing status of the uploaded PDF file.</p>

<ul>
  <li><strong>http://127.0.0.1:8000/docs#/default/polling_polling__post</strong> <code></code></li>
  <li><strong>Method:</strong> POST</li>
  <li><strong>Request Body:</strong>
    <ul>
      <li><code>pdf_id</code>: Unique identifier of the uploaded PDF.</li>
    </ul>
  </li>
  <li><strong>Response:</strong>
    <ul>
      <li>If the processing is complete:
        <pre><code>{
    "pdf_id": "your_pdf_id",
    "status": "completed"
}
</code></pre></li>
      <li>If the processing is still in progress:
        <pre><code>{
    "detail": "File is processing, please wait."
}
</code></pre></li>
    </ul>
  </li>
</ul>

<h2>Testing</h2>

<h3>Using FastAPI Swagger UI</h3>

<ol>
  <li>Navigate to <code>http://127.0.0.1:8000/docs</code> in your web browser.</li>
  
<li><strong>http://127.0.0.1:8000/docs#/</strong><code></code></li>
  <li>Upload a PDF file using the <code>/webhook/</code> endpoint.</li>
  <li>Check the processing status using the <code>/polling/</code> endpoint.</li>
</ol>

<h3>Webhook Test Site</h3>

<p>You can use the provided webhook test site to receive the <code>pdf_id</code> and <code>text</code> data simultaneously:</p>

<p><a href="https://webhook.site/#!/view/cdbb1b50-031c-4901-8429-a1c88d10767a/720edd61-1e0d-46db-b53c-0afb9617e532/1">https://webhook.site/#!/view/cdbb1b50-031c-4901-8429-a1c88d10767a/720edd61-1e0d-46db-b53c-0afb9617e532/1</a></p>

<p>Use this URL as the webhook endpoint to receive the data when processing is complete.</p>

<h2>Contributing</h2>

<p>Contributions are welcome! Please open an issue or submit a pull request with any enhancements or bug fixes.</p>

<h2>License</h2>

<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
