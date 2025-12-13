<?php
session_start();
require_once 'db.php';

if (isset($_POST['uid'], $_POST['pwd'])) {

    $username = trim($_POST['uid']);
    $password = $_POST['pwd'];

    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = ? LIMIT 1");
    $stmt->execute([$username]);
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    if (!$user) {
        header("Location: success.php?msg=Napačno uporabniško ime.&type=error");
        exit;
    }

    if (!$user['is_active']) {
        header("Location: success.php?msg=Račun ni aktiviran.&type=error");
        exit;
    }

    if (password_verify($password, $user['password'])) {
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];

        header("Location: main.php");
        exit;
    }

    header("Location: success.php?msg=Napačno geslo.&type=error");
    exit;
}
