<?php
session_start();
error_reporting(E_ERROR | E_WARNING | E_PARSE);
$dbServername = "localhost:3308";
$dbUsername = "root";
$dbPassword = "";
$dbName = "sih";

$conn = mysqli_connect($dbServername, $dbUsername, $dbPassword, $dbName);

$sql_delete1 = "TRUNCATE TABLE dark";
mysqli_query($conn,$sql_delete1);
$sql_delete2 = "TRUNCATE TABLE surface";
mysqli_query($conn,$sql_delete2);
?>

<!DOCTYPE html>
<html>
<head>
	<title>CrawlBot</title>
	<link rel="stylesheet" type="text/css" href="web.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

	<script>
		$(document).ready(function()
		{
			setInterval(function()
			{
				$(active_links).load("active_links.php");
				refresh();
			},5000)
		})
	</script>
</head>
<body>
<h1>CrawlBot</h1>
<?php
if($_SESSION['disp'] == 'on'){
	$key = $_SESSION['key'];
	$webtype = $_SESSION['type'];
	$number = $_SESSION['num'];
?>
	<form action="web.php" method="POST">
		<div class="container">
		<label>Keyword Search           </label>
		<input type="text" name="key" value="<?php echo $key ?>" required style="margin-left:80px " >
		<br>
		<label>Depth of Crawl </label>
		<input type="text" name="num" value="<?php echo $number ?>" style="margin-left:87px " required>
		<br>
		<label>Type of web</label>
		<select name="type" style="margin-left:107px;margin-top: 10px;" required>
			<!-- <option value="" disabled selected>None</option> -->
			<?php
			if($webtype == "surface"){
			?>
				<option value="surface" selected>Surface Web</option>
				<option value="dark">Dark Web</option>
			<?php
			}else{
			?>
				<option value="surface">Surface Web</option>
				<option value="dark" selected>Dark Web</option>
			<?php
			}
			?>
		</select>
		<br>
		<button id="but" name = "submit" value="5" style="margin-left:191px">Submit</button>
		<br><br>
		</div>
	</form>
<?php
	$_SESSION['disp'] = 'off';
}else{
?>
	<form action="web.php" method="POST">
		<div class="container">
		<label>Keyword Search           </label>
		<input type="text" name="key" required style="margin-left:80px " >
		<br>
		<label>Depth of Crawl </label>
		<input type="text" name="num"style="margin-left:87px " required>
		<br>
		<label>Type of web</label>
		<select name="type" style="margin-left:107px;margin-top: 10px;" required>
			<option value="" disabled selected>None</option>
			<option value="surface">Surface Web</option>
			<option value="dark">Dark Web</option>
		</select>
		<br>
		<button id="but" name = "submit" value="5" style="margin-left:191px">Submit</button>
		<br><br>
		</div>
	</form>
<?php
}
?>


<?php
function execInBackground($cmd) {
    if (substr(php_uname(), 0, 7) == "Windows"){
        pclose(popen("start /B ". $cmd, "r"));
    }
    else {
        exec($cmd . " > /dev/null &"); 
    }
}
?>

<?php
ini_set('max_execution_time', 600);
if(isset($_POST['submit'])){
	$_SESSION['disp'] = 'on';
	$key = $_POST['key'];
	$_SESSION['key'] = $key;
	$webtype = $_POST['type'];
	$_SESSION['type'] = $webtype;
	$number = $_POST['num'];
	$_SESSION['num'] = $number;
	if($webtype=="surface"){
		execInBackground("python surface_crawler.py $key $number > out_surface.log");
		header("Refresh:0");
	}else{
		execInBackground("python dark_crawler.py $key $number > out_dark.log");
		header("Refresh:0");
	}
}
?>
<div style="margin-left: 40px; height:350px;width:1050px;border:1px solid #ccc;font:16px/26px Georgia, Garamond, Serif;overflow:auto; color:white;" id="active_links">
Search Results
</div>
</body>
</html>