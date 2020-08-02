<?php

$dbServername = "localhost:3308";
$dbUsername = "root";
$dbPassword = "";
$dbName = "sih";

$conn = mysqli_connect($dbServername, $dbUsername, $dbPassword, $dbName);

$sql_dark = "SELECT * FROM dark";
$result_dark = mysqli_query($conn,$sql_dark);
$num_dark = mysqli_num_rows($result_dark);

$sql_surface = "SELECT * FROM surface";
$result_surface = mysqli_query($conn,$sql_surface);
$num_surface = mysqli_num_rows($result_surface);

$total_links = $num_dark + $num_surface
?>


<!-- Content Row -->
<div class="row">

<!-- Earnings (Monthly) Card Example -->
<div class="col-xl-4 col-md-6 mb-4" onclick="location.href='tables.php?val=tables'" style="cursor: pointer;">
  <div class="card border-left-primary shadow h-100 py-2">
    <div class="card-body">
      <div class="row no-gutters align-items-center">
        <div class="col mr-2">
          <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">Number of Links crawled</div>
          <div class="h5 mb-0 font-weight-bold text-gray-800"><?php echo $total_links ?></div>
        </div>
        <!--<div class="col-auto">
          <i class="fas fa-calendar fa-2x text-gray-300"></i>
        </div>-->
      </div>
    </div>
  </div>
</div>

<!-- Earnings (Monthly) Card Example -->
<div class="col-xl-4 col-md-6 mb-4" onclick="location.href='tables.php?val=tables'" style="cursor: pointer;">
  <div class="card border-left-success shadow h-100 py-2">
    <div class="card-body">
      <div class="row no-gutters align-items-center">
        <div class="col mr-2">
          <div class="text-xs font-weight-bold text-success text-uppercase mb-1">Dark web Links</div>
          <div class="h5 mb-0 font-weight-bold text-gray-800"><?php echo $num_dark ?></div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Earnings (Monthly) Card Example -->

<!-- Pending Requests Card Example -->
<div class="col-xl-4 col-md-6 mb-4" onclick="location.href='tables.php?val=tables'" style="cursor: pointer;">
  <div class="card border-left-warning shadow h-100 py-2">
    <div class="card-body">
      <div class="row no-gutters align-items-center">
        <div class="col mr-2">
          <div class="text-xs font-weight-bold text-warning text-uppercase mb-1">Surface web Links</div>
          <div class="h5 mb-0 mr-3 font-weight-bold text-gray-800"><?php echo $num_surface ?>
          </div>
        </div>
        <!--
        <div class="col" style="padding-top: 50px; width: 10px;">
          <div class="progress progress-sm mr-2">
             <div class="progress-bar bg-info" role="progressbar" style="width: 94%;" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
        </div>
      -->
      </div>
    </div>
  </div>
</div>
</div>