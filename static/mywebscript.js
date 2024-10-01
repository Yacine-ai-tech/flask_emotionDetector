let RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4) { // Check if the request is complete
            if (this.status === 200) {
                // If successful, display the response text
                document.getElementById("system_response").innerHTML = xhttp.responseText;
            } else {
                // If there was an error, parse and display the error message
                try {
                    const errorResponse = JSON.parse(xhttp.responseText);
                    document.getElementById("system_response").innerHTML = errorResponse.error;
                } catch (e) {
                    // Handle case where response is not valid JSON
                    document.getElementById("system_response").innerHTML = "An error occurred: " + xhttp.responseText;
                }
            }
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
};
