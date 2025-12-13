<?php
// recover.php – brez pošiljanja emaila (lokalna verzija)

if (isset($_POST['email'])) {

    // Tukaj bi bila logika za pošiljanje emaila, če bi bilo omogočeno.
    // Ker trenutno nimaš PHPMailerja in SMTP, naredimo obvestilo:

    header("Location: success.php?msg=Ponastavitev gesla trenutno ni mogoča.&type=error");
    exit();
}
?>
