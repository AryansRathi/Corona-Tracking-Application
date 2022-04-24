<?php 

$server = "localhost";
$user = "group5";
$pass = "hz2aAr";
$database = "group5";

$conn = mysqli_connect($server, $user, $pass, $database);

if (!$conn) {
    die("<script>alert('Connection Failed.')</script>");
}

?>
