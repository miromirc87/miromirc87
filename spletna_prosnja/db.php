<?php
$host = "sql206.infinityfree.com";
$user = "if0_40656663";
$pass = "Kissik488xKra1t";
$db   = "if0_40656663_miromirc";

try {
    $pdo = new PDO(
        "mysql:host=$host;dbname=$db;charset=utf8",
        $user,
        $pass,
        [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]
    );
} catch (PDOException $e) {
    exit; // brez echo
}
