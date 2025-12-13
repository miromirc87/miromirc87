<?php
include 'db.php';

if(isset($_GET['code'])){
    $code = $_GET['code'];
    $stmt = $pdo->prepare("SELECT * FROM users WHERE activation_code = ?");
    $stmt->execute([$code]);
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    if($user){
        $stmt = $pdo->prepare("UPDATE users SET is_active = 1, activation_code = NULL WHERE id = ?");
        $stmt->execute([$user['id']]);
        header("Location: success.php?msg=Račun je aktiviran! Sedaj se lahko prijavite.&type=success");
        exit();
    } else {
        header("Location: success.php?msg=Neveljavna aktivacijska koda.&type=error");
        exit();
    }
}
?>
