<?php
// Include config file
require_once "Config.php";

// Define variables and initialize with empty values
$upload_err = "";
$success_message = "";

// Processing file upload when form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Check if a file is selected
    if (isset($_FILES["csv_file"]) && $_FILES["csv_file"]["error"] == UPLOAD_ERR_OK) {
        // Get file details
        $file_name = $_FILES["csv_file"]["name"];
        $file_size = $_FILES["csv_file"]["size"];
        $file_tmp = $_FILES["csv_file"]["tmp_name"];
        $file_type = $_FILES["csv_file"]["type"];

        // Check file extension
        $file_ext = strtolower(pathinfo($file_name, PATHINFO_EXTENSION));
        $allowed_ext = array("csv");

        if (in_array($file_ext, $allowed_ext)) {
            // Move uploaded file to a temporary location
            if (move_uploaded_file($file_tmp, "uploads/" . $file_name)) {
                // File uploaded successfully
                $success_message = "File uploaded successfully.";
            } else {
                $upload_err = "Error occurred while uploading the file.";
            }
        } else {
            $upload_err = "Invalid file extension. Only CSV files are allowed.";
        }
    } else {
        $upload_err = "Please select a CSV file to upload.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>CSV File Upload</title>
    <link rel="stylesheet" href=""> //need to be adjusted
    <style>
        body {
            font: 14px sans-serif;
        }

        .wrapper {
            width: 360px;
            padding: 20px;
        }
    </style>
</head>

<body>
    <div class="wrapper">
        <h2>CSV File Upload</h2>
        <p>Please select a CSV file to upload.</p>
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post" enctype="multipart/form-data">
            <div class="form-group">
                <label>CSV File</label>
                <input type="file" name="csv_file" class="form-control-file <?php echo (!empty($upload_err)) ? 'is-invalid' : ''; ?>">
                <span class="invalid-feedback"><?php echo $upload_err; ?></span>
            </div>
            <div class="form-group">
                <input type="submit" class="btn btn-primary" value="Upload">
            </div>
        </form>
        <?php if (!empty($success_message)) : ?>
            <div class="alert alert-success"><?php echo $success_message; ?></div>
        <?php endif; ?>
    </div>
</body>

</html>