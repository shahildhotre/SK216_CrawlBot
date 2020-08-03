<?php
$dbServername = "localhost:3308";
$dbUsername = "root";
$dbPassword = "";
$dbName = "sih";

$conn = mysqli_connect($dbServername, $dbUsername, $dbPassword, $dbName);

// get Users
$query = "SELECT * FROM dark";
if (!$result = mysqli_query($conn, $query)) {
    exit(mysqli_error($conn));
}
 
$users = array();
if (mysqli_num_rows($result) > 0) {
    while ($row = mysqli_fetch_assoc($result)) {
        $users[] = $row;
    }
}
 
header('Content-Type: text/csv; charset=utf-8');
header('Content-Disposition: attachment; filename=dark_web.csv');
$output = fopen('php://output', 'w');
fputcsv($output, array('ID','Link URL','Link status'));
 
if (count($users) > 0) {
    foreach ($users as $row) {
        fputcsv($output, $row);
    }
}




//header("Location: download_surface.php");
?>