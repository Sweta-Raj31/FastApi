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

<h2>Usage</h2>

<h3>Webhook Endpoint</h3>

<h4>Description:</h4>

<p>This endpoint allows you to upload a PDF file, which will be processed and the extracted text data will be sent to a specified webhook URL.</p>

<ul>
  <li><strong>URL:</strong> <code>/webhook/</code></li>
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

<h4>Testing Instructions:</h4>

<ol>
  <li>Use any API testing tool like Postman or cURL to send a POST request to the <code>/webhook/</code> endpoint.</li>
  <li>Attach a PDF file to the request body using the <code>file</code> parameter.</li>
  <li>Send the request to upload the PDF file.</li>
  <li>Verify that the response contains the <code>pdf_id</code> and <code>text</code> extracted from the PDF.</li>
</ol>

<h3>Polling Endpoint</h3>

<h4>Description:</h4>

<p>This endpoint allows you to check the processing status of the uploaded PDF file.</p>

<ul>
  <li><strong>URL:</strong> <code>/polling/</code></li>
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

<h4>Testing Instructions:</h4>

<ol>
  <li>Use any API testing tool like Postman or cURL to send a POST request to the <code>/polling/</code> endpoint.</li>
  <li>Provide the <code>pdf_id</code> of the uploaded PDF file in the request body.</li>
  <li>Send the request to check the processing status.</li>
  <li>Verify the response to see if the processing is completed or still in progress.</li>
</ol>

<h2>Contributing</h2>

<p>Contributions are welcome! Please open an issue or submit a pull request with any enhancements or bug fixes.</p>

<h2>License</h2>

<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
