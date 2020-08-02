<!-- Sidebar -->
<ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" id="accordionSidebar">

  <!-- Sidebar - Brand -->
  <a class="sidebar-brand d-flex align-items-center justify-content-center" href="index.php">
    <div class="sidebar-brand-icon">
      <!--<i class="fas fa-laugh-wink"></i>-->
      <i class="fas fa-university"></i>
    </div>
    <h2 class="sidebar-brand-text mx-3" style="padding-top: 10px;">VJTI</h2>
  </a>

  <!-- Divider -->
  <hr class="sidebar-divider my-0">

  <!-- Nav Item - Dashboard -->
  <li <?php if($_GET['val'] == ''){echo "class='nav-item active'";}else{echo "class='nav-item'";}?> >
    <a class="nav-link" href="index.php">
      <i class="fas fa-fw fa-tachometer-alt"></i>
      <span style="margin-bottom: 110px">Dashboard</span></a>
  </li>
  <!-- Nav Item - Pages Collapse Menu 
  <li class="nav-item">
    <a class="nav-link" href="graph.php">
      <i class="fas fa-fw fa-chart-area"></i>
      <span>Link Statistics</span></a>
  </li>-->

  <!-- Nav Item - Utilities Collapse Menu -->
  <li <?php if($_GET['val'] == 'tables'){echo "class='nav-item active'";}else{echo "class='nav-item'";}?> >
    <a class="nav-link" href="tables.php?val=tables">
      <i class="fas fa-fw fa-chart-area"></i>
      <span id=>Links Crawled</span></a>
  </li>

  <!-- Nav Item - Pages Collapse Menu -->
  <li <?php if($_GET['val'] == 'actives'){echo "class='nav-item active'";}else{echo "class='nav-item'";}?>>
    <a class="nav-link" href="active.php?val=actives" >
      <i class="fas fa-fw fa-chart-area"></i>
      <span>Links Status</span></a>
  </li>

  <!-- Nav Item - Charts -->
  <li <?php if($_GET['val'] == 'sitemap'){echo "class='nav-item active'";}else{echo "class='nav-item'";}?>>
    <a class="nav-link" href="sitemap.php?val=sitemap">
      <i class="fas fa-fw fa-chart-area"></i>
      <span>Link Map</span></a>
  </li>

  <li <?php if($_GET['val'] == 'flag'){echo "class='nav-item active'";}else{echo "class='nav-item'";}?>">
    <a class="nav-link" href="flag.php?val=flag">
      <i class="fas fa-fw fa-chart-area"></i>
      <span>Flag A Page</span></a>
  </li>

  <!-- Divider -->
  <hr class="sidebar-divider d-none d-md-block">

  <!-- Sidebar Toggler (Sidebar) -->
  <div class="text-center d-none d-md-inline">
    <button class="rounded-circle border-0" id="sidebarToggle"></button>
  </div>

</ul>
<!-- End of Sidebar -->