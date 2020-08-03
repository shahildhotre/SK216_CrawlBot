<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Dashboard</title>

  <!-- Custom fonts for this template-->
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">

  <!-- Custom styles for this template-->
  <link href="css/sb-admin-2.css" rel="stylesheet">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

  <script>
    $(document).ready(function()
    {
      setInterval(function()
      {
        $(update_val).load("num_autoload.php");
        refresh();
      },500)
    })
  </script>

</head>

<body id="page-top">

  <!-- Page Wrapper -->
  <div id="wrapper">

    <?php
    $_GET['val'] = '';
    require_once("slidebar.php");
    ?>

    <!-- Content Wrapper -->
    <div id="content-wrapper" class="d-flex flex-column">
      <!-- Main Content -->
       
        <!-- End of Topbar -->

        <!-- Begin Page Content -->
        <div class="container-fluid">



			<div class="container" style="padding-top: 10px">
				<h1 style="display: inline-block; text-align: center;padding-left: 35%;">Crawl Bot</h1>
			</div>

      <!-- Divider -->
      <hr class="sidebar-divider my-0">
			
          <!-- Page Heading -->
          <div class="d-sm-flex align-items-center justify-content-between mb-4">
            <h1 class="h3 mb-0 text-gray-800">Dashboard</h1>
          </div>

          <div id="update_val">
            <!-- Content Row -->
            <div class="row">

            <!-- Earnings (Monthly) Card Example -->
            <div class="col-xl-4 col-md-6 mb-4" onclick="location.href='tables.php?val=tables'" style="cursor: pointer;">
              <div class="card border-left-primary shadow h-100 py-2">
                <div class="card-body">
                  <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                      <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">Number of Links crawled</div>
                      <div class="h5 mb-0 font-weight-bold text-gray-800">0</div>
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
                      <div class="h5 mb-0 font-weight-bold text-gray-800">0</div>
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
                      <div class="h5 mb-0 mr-3 font-weight-bold text-gray-800">0
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
          </div>

          <!-- Content Row -->

          <!--<div class="row">

            <!-- Pie Chart -->
            <div class="col-xl-12 col-lg-5">
              <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                  <h6 class="m-0 font-weight-bold text-primary">Active - Inactive Links</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body">
                  <div class="chart-pie pt-4 pb-2">
                    <canvas id="myPieChart"></canvas>
                  </div>
                  <div class="mt-6 text-center small">
                    <span class="mr-2">
                      <i class="fas fa-circle text-primary"></i> Active links
                    </span>
                    <span class="mr-2">
                      <i class="fas fa-circle text-success"></i> Inactive links
                    </span>
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

  <!-- Page level custom scripts -->
  
  <script src="js/demo/chart-pie-demo.js"></script>

</body>

</html>
