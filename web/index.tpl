<!DOCTYPE HTML>
<html>
	<head>
		<title>Sport en Pays de la Loire</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<!--[if lte IE 8]><script src="js/ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="css/main.css" />
		<!--[if lte IE 8]><link rel="stylesheet" href="css/ie8.css" /><![endif]-->
	</head>
	<body>

		<!-- Header -->
			<section id="header">
				<header>
					<h1>Rechercher une activitée sportive en Pays de la Loire</h1>
					<p>Pauline Chabaud et Corentin May</p>
					<br>
					<br>
				</header>
				<footer>
					<a href="#first" class="button style2 scrolly-middle">Lieux où pratiqué une activitée</a>
					<a href="#second" class="button style2 scrolly-middle">Liste des activitées dans ma ville</a>
					<a href="#tree" class="button style2 scrolly-middle">Activitée dans ma ville</a>
				</footer>
			</section>


			<!-- Banner -->
						<section id="banner">
							<header>
								<h2>Activitées sportive en Pays de la Loire</h2>
							</header>
							<p>Ce site permet de rechercher les activitées sportives disponnibles en Pays de la Loire</p>
							<img src="images/logoPDL.jpg" alt="" />
						</section>

			<!-- Feature 1 -->
						<article id="first" class="container box style1 right">


								<header>
									<h2>Recherche du lieux où est pratiqué l'activité :</h2>
									<form method="GET" action="/search">
												<div class="row 50%">
												<div class="12u$">
													<ul class="actions">
														<li><select class="" name="activity">
											        % for o in data:
											          <option value="{{o.name_activity}}">{{o.name_activity}}</option>
											        % end
											      </select></li>
														<br>
														<br>
														<li>
									      <input type="submit" name="name" value="Rechercher">
											</li>
										</div>
										<br/>
									</div>
							    </form>
								</header>
						</article>

						<!-- Feature 1 -->
									<article id="second" class="container box style1 right">


											<header>
												<h2>Recherche des activités disponibles dans ma ville :</h2>
													<form class="" action="/city" method="post">
														<div class="row 50%">
															<div class="12u$">
																<ul class="actions">
																	<li><select class="" name="city">
														        % for o in data_city:
														          <option value="{{o}}">{{o}}</option>
														        % end
														      </select></li>
																	<br>
																	<br>
																	<li>
												      <input type="submit" name="name" value="Rechercher">
														</li>
													</ul>
													</div>
													<br/>
												</div>
										    </form>
											</header>
									</article>



	<!-- Feature 1 -->
				<article id="tree" class="container box style1 right">


						<header>
							<h2>Recherche une activitée dans ma ville :</h2>
								<form class="" action="/activity" method="get">
									<div class="row 50%">
										<div class="6u 12u$(mobile)"><select class="" name="city">
							        % for o in data_city:
							          <option value="{{o}}">{{o}}</option>
							        % end
							      </select></div>
										<div class="6u 12u$(mobile)"><select class="" name="activity">
							        % for o in data:
							          <option value="{{o.id}}">{{o.name_activity}}</option>
							        % end
							      </select></div>
										<div class="12u$">
											<ul class="actions">
												<li>
							      <input type="submit"  value="Rechercher">
									</li>
								</ul>
								</div>
								<br/>
							</div>
					    </form>
						</header>
				</article>



          <!-- Scripts -->
    			<script src="js/jquery.min.js"></script>
    			<script src="js/jquery.scrolly.min.js"></script>
    			<script src="js/jquery.poptrox.min.js"></script>
    			<script src="js/skel.min.js"></script>
    			<script src="js/util.js"></script>
    			<!--[if lte IE 8]><script src="js/ie/respond.min.js"></script><![endif]-->
    			<script src="js/main.js"></script>


					<section id="footer">

								<div class="copyright">
									<ul class="menu">
										<li>&copy; Pauline CHABAUD et Corentin MAY</li><li>Données : <a href="http://data.paysdelaloire.fr/">http://data.paysdelaloire.fr/</a></li>
									</ul>
								</div>
							</section>
  </body>
</html>
