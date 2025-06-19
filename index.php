<?php
// index.php

// Configuration
define('TEXT_DIR', __DIR__ . '/txtFiles (1 - 10000)');
define('MIN_FILE', 1);
define('MAX_FILE', 10000);

$fileContent = '';
$error       = '';
$byteCount   = null;  // ← New: will hold the file size

// Handle user input
if (isset($_GET['file'])) {
    // Cast to int and clamp
    $num = (int) $_GET['file'];
    if ($num < MIN_FILE || $num > MAX_FILE) {
        $error = "Please enter a number between " . MIN_FILE . " and " . MAX_FILE . ".";
    } else {
        // Pad with zeros to 6 digits
        $padded  = str_pad($num, 6, '0', STR_PAD_LEFT);
        $filename = TEXT_DIR . "/FILE-{$padded}.txt";
        
        if (!is_readable($filename)) {
            $error = "File #{$num} not found.";
        } else {
            // Read the entire file
            $fileContent = file_get_contents($filename);
            if ($fileContent === false) {
                $error = "Failed to read file.";
            } else {
                // ← New: get byte count
                $byteCount = strlen($fileContent);
            }
        }
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Text Viewer</title>
  <style>
    body {
      font-family: sans-serif;
      background: #f0f2f5;
      margin: 0;
      padding: 2rem;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .container {
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
      padding: 1.5rem;
      max-width: 800px;
      width: 100%;
    }
    h1 {
      margin-top: 0;
      font-size: 1.5rem;
    }
    form {
      margin-bottom: 1rem;
    }
    input[type="number"] {
      width: 6rem;
      padding: 0.4rem;
      font-size: 1rem;
      margin-right: 0.5rem;
    }
    button {
      padding: 0.5rem 1rem;
      font-size: 1rem;
      border: none;
      background: #4a90e2;
      color: #fff;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background: #357ab8;
    }
    .error {
      color: #c00;
      margin-bottom: 1rem;
    }
    .byte-count {
      font-size: 0.9rem;
      color: #555;
      margin-bottom: 0.5rem;
    }
    pre {
      background: #fafafa;
      padding: 1rem;
      border: 1px solid #ddd;
      border-radius: 4px;
      max-height: 70vh;
      overflow: auto;
      white-space: pre-wrap;
      word-wrap: break-word;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Text Viewer</h1>
    <form method="get" action="">
      <label for="file">File # (1-10000):</label>
      <input
        type="number"
        id="file"
        name="file"
        min="<?php echo MIN_FILE ?>"
        max="<?php echo MAX_FILE ?>"
        value="<?php echo isset($_GET['file']) ? htmlspecialchars($_GET['file']) : '' ?>"
        required
      >
      <button type="submit">Load</button>
    </form>

    <?php if ($error): ?>
      <div class="error"><?php echo htmlspecialchars($error) ?></div>
    <?php endif; ?>

    <?php if ($fileContent !== ''): ?>
      <!-- NEW: display byte count -->
      <div class="byte-count">
        File size: <?php echo number_format($byteCount) ?> bytes
      </div>
      <pre><?php echo htmlspecialchars($fileContent) ?></pre>
    <?php endif; ?>
  </div>
</body>
</html>
