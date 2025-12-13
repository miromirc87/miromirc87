<?php
include 'db.php';

if (isset($_POST['user'], $_POST['email'], $_POST['pwd'], $_POST['pwd1'])) {

    $username = trim($_POST['user']);
    $email    = trim($_POST['email']);
    $pwd      = $_POST['pwd'];
    $pwd1     = $_POST['pwd1'];

    // 1️⃣ Validacija uporabniškega imena
    if (strlen($username) < 4) {
        header("Location: success.php?msg=Uporabniško ime mora imeti vsaj 4 znake.&type=error");
        exit();
    }

    // 2️⃣ Validacija emaila
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        header("Location: success.php?msg=Vnesen email ni veljaven.&type=error");
        exit();
    }

    // 3️⃣ Validacija gesla
    if (strlen($pwd) < 8) {
        header("Location: success.php?msg=Geslo mora imeti vsaj 8 znakov.&type=error");
        exit();
    }

    // 4️⃣ Preveri ujemanje gesel
    if ($pwd !== $pwd1) {
        header("Location: success.php?msg=Gesli se ne ujemata.&type=error");
        exit();
    }

    // 5️⃣ Preveri, ali username ali email že obstajata
    $stmt = $pdo->prepare("SELECT id FROM users WHERE username = ? OR email = ?");
    $stmt->execute([$username, $email]);

    if ($stmt->fetch()) {
        header("Location: success.php?msg=Uporabniško ime ali email je že zaseden.&type=error");
        exit();
    }

    // 6️⃣ Hashiranje gesla
    $hashedPwd = password_hash($pwd, PASSWORD_DEFAULT);

    // 7️⃣ Vstavi uporabnika kot NEAKTIVNEGA
    $stmt = $pdo->prepare("
        INSERT INTO users (username, email, password, is_active)
        VALUES (?, ?, ?, 0)
    ");
    $stmt->execute([$username, $email, $hashedPwd]);

    // 8️⃣ Uspeh
    header("Location: success.php?msg=Registracija uspešna. Račun mora biti aktiviran.&type=success&redirect=index.html");
    exit();
}
?>
