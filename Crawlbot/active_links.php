<?php

$dbServername = "localhost:3308";
$dbUsername = "root";
$dbPassword = "";
$dbName = "sih";

$conn = mysqli_connect($dbServername, $dbUsername, $dbPassword, $dbName);

$sql = "SELECT * FROM dark WHERE `link_status` ='Active'";
$result = mysqli_query($conn,$sql);
$num = mysqli_num_rows($result);

$sql_surface = "SELECT * FROM surface WHERE `link_status` ='Active'";
$result_surface = mysqli_query($conn,$sql_surface);
$num_surface = mysqli_num_rows($result_surface);

echo "Search Results";
echo "<br>";

if($num>0){
	while($row = $result->fetch_assoc()){
		$linkdisp = "<a href=".$row['link_url']." style='color:white; margin-left:20px; font-size:1.2em;'>".$row['link_url']."</a>";
		echo $linkdisp;
		echo "<br>";
		echo "<br>";
	}
}

if($num_surface>0){
	while($row = $result_surface->fetch_assoc()){
		$linkdisp = "<a href=".$row['link_url']." style='color:white; margin-left:20px; font-size:1.2em;'>".$row['link_url']."</a>";
		echo $linkdisp;
		echo "<br>";
		echo "<br>";
	}
}