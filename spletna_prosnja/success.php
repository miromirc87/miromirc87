<?php
$msg = $_GET['msg'] ?? '';
$type = $_GET['type'] ?? 'success'; // success ali error
$redirect = $_GET['redirect'] ?? 'index.html';
$time = $_GET['time'] ?? 3; // sekunde
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Obvestilo :: miro.mirc</title>
    <link rel="stylesheet" href="style.css">
    <?php if($type == 'success'): ?>
    <meta http-equiv="refresh" content="<?= $time ?>;url=<?= $redirect ?>">
    <?php endif; ?>
</head>
<body>
<div class="center-wrapper">
    <div class="signin-box">
        <h2><font color="#fe9b02">miro</font>.mirc</h2>
        <h3 class="signin-title-secondary">
            <?= htmlspecialchars($msg) ?>
        </h3>
        <?php if($type == 'success'): ?>
        <p>Preusmeritev čez <?= $time ?> sekunde...</p>
        <?php else: ?>
        <p><a href="index.html">Nazaj na prijavo</a></p>
        <?php endif; ?>
    </div>
</div>
</body>
</html>
