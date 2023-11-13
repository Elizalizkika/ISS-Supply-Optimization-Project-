<?php
    session_start();

    if(isset($$_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
        header("loaction: welcome.php");
        exit;
    }

    require_once 'Config.php'; //changed to single quotes due to syntax error
    $username = $password = "";
    $username_err = $password_err = $login_err = "";

    if($_SERVER["REQUEST_METHOD"] == "POST"){
        if(empty(trim($_POST["username"]))){
            $username_err = "Please enter username.";
        } else{
            $username = trim($_POST["username"]);
        }
        
        if(empty(trim($_POST["password"]))){
            $password_err = "Please enter your password.";
        } else{
            $password = trim($_POST["password"]);
        }

        if(empty($username_err) && empty($password_err)){
            $sql = "SELECT id, username, password FROM users WHERE username = ?";
            
            if 
        }
    }