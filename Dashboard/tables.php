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
?>

<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Crawl Bot</title>

  <!-- Custom fonts for this template-->
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">
  <!--Datatables-->
  <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.21/css/jquery.dataTables.min.css">
  <!-- Custom styles for this template-->
  <link href="css/sb-admin-2.css" rel="stylesheet">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

</head>

<body id="page-top">

  <!-- Page Wrapper -->
  <div id="wrapper">

    <!-- Sidebar -->
    <?php
    require_once("slidebar.php")
    ?>
    <!-- End of Sidebar -->

    <!-- Content Wrapper -->
    <div id="content-wrapper" class="d-flex flex-column">
      <!-- Main Content -->
       
        <!-- End of Topbar -->

        <!-- Begin Page Content -->
        <div class="container-fluid">



      <div class="container" style="padding-top: 10px">
        <h1 style="display: inline-block; text-align: center;padding-left: 35%">Crawl Bot</h1>
      </div>

      <!-- Divider -->
      <hr class="sidebar-divider my-0">
      
        <!-- End of Topbar -->

      <div class="d-sm-flex align-items-center justify-content-between mb-4">
          <h1 class="h3 mb-0 text-gray-800">Links Crawled</h1>
        </div>

        <!-- Begin Page Content -->

          <!-- DataTales Example -->

          <div class="row">

            <!-- Earnings (Monthly) Card Example -->
            <div class="col-xl-12 col-md-6" >
              <div class="card shadow mb-4">
                
                <!-- Tab links -->
                <div class="tab">
                  <button class="tablinks active" onclick="openData(event, 'Dark')">Dark web</button>
                  <button class="tablinks" onclick="openData(event, 'Surface')">Surface web</button>
                  <button id="nohover" style="color: white; margin-left: 65%;"><a href="download_csv.php" >Export CSV</a></button>
                  <!--<button class="button" style="color: white; margin-left: 65%;">Export CSV</bupx;tton>-->
                </div>

                
                <div id="Dark" class="tabcontent" style="display: block;">
                  <div class="card-body">
                    <div class="table-responsive">
                      <table class="table table-bordered dataTable" cellspacing="0" width="100%" data-page-length="25">
                        <col width="100px" />
                        <col width="780px" />
                        <col width="150px" />

                        <thead>
                          <tr>
                            <th>Index</th>
                            <th>Links</th>
                            <th>Status</th>
                          </tr>
                        </thead>                    
                        
                        <tbody>
                          <?php
                          if($num_dark>0){
                              while($row = $result_dark->fetch_assoc()){
                                echo "<tr>";
                                    echo "<td>".($row['ID'])."</td>";
                                    echo "<td>".$row['link_url']."</td>";
                                    echo "<td>".$row['link_status']."</td>";
                                    echo "</tr>";
                              }
                            }
                            ?>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>

                <div id="Surface" class="tabcontent">
                  <div class="card-body">
                    <div class="table-responsive">
                      <table class="table table-bordered dataTable" cellspacing="0" width="100%" data-page-length="25">
                        <col width="100px" />
                        <col width="780px" />
                        <col width="150px" />

                        <thead>
                          <tr>
                            <th>Index</th>
                            <th>Links</th>
                            <th>Status</th>
                          </tr>
                        </thead>

                        <tbody>
                          <?php
                          if($num_surface>0){
                              while($row = $result_surface->fetch_assoc()){
                                echo "<tr>";
                                echo "<td>".($row['ID'])."</td>";
                                echo "<td>".$row['link_url']."</td>";
                                echo "<td>".$row['link_status']."</td>";
                                echo "</tr>";
                              }
                            }
                            ?>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>

              </div>

        </div>
      </div>
    </div>
        <!-- /.container-fluid -->

      </div>
      <!-- End of Main Content -->

     </div>
    <!-- End of Content Wrapper -->

  </div>
  <!-- End of Page Wrapper -->

  <!-- Scroll to Top Button-->
  <a class="scroll-to-top rounded" href="#page-top">
    <i class="fas fa-angle-up"></i>
  </a>


  <!-- Bootstrap core JavaScript-->
  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Core plugin JavaScript-->
  <script src="vendor/jquery-easing/jquery.easing.min.js"></script>

  <!-- Custom scripts for all pages-->
  <script src="js/sb-admin-2.min.js"></script>

  <!-- Page level plugins -->
  <script src="vendor/chart.js/Chart.min.js"></script>

  

<script src="https://code.jquery.com/jquery-3.5.1.js"></script>
<script src="https://cdn.datatables.net/1.10.21/js/jquery.dataTables.min.js"></script>

  <script>
  $(document).ready(function(){
      $('.dataTable').dataTable();
  });


  function openData(evt, web_type) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(web_type).style.display = "block";
    evt.currentTarget.className += " active";
  }

  </script>
</body>

</html>
