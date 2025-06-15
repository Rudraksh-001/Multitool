<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook Token Tools Suite</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        /* Global Styles */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
        }

        .page {
            display: none;
            min-height: 100vh;
        }

        .page.active {
            display: block;
        }

        /* Navigation */
        .navbar {
            background: linear-gradient(135deg, #1877f2, #166fe5);
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .navbar-brand {
            font-weight: bold;
            color: white !important;
        }

        .nav-link {
            color: rgba(255,255,255,0.8) !important;
            transition: color 0.3s;
        }

        .nav-link:hover,
        .nav-link.active {
            color: white !important;
        }

        /* Token Checker Styles */
        #tokenChecker {
            background-color: #f0f2f5;
        }

        #tokenChecker .container {
            max-width: 600px;
            margin-top: 50px;
        }

        #tokenChecker .card {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        #tokenChecker .card-header {
            background-color: #1877f2;
            color: white;
            border-radius: 10px 10px 0 0 !important;
        }

        #tokenChecker .btn-primary {
            background-color: #1877f2;
            border-color: #1877f2;
        }

        #tokenChecker .btn-primary:hover {
            background-color: #166fe5;
            border-color: #166fe5;
        }

        #tokenChecker .result-box {
            background-color: #f7f7f7;
            border-radius: 5px;
            padding: 15px;
            margin-top: 20px;
        }

        #tokenChecker .error-message {
            color: #dc3545;
            font-weight: bold;
        }

        /* Server 1 Styles */
        #server1 {
            background-color: black;
            color: white;
            position: relative;
            overflow: hidden;
        }

        #server1 .video-background {
            position: fixed;
            top: 50%;
            left: 50%;
            width: 100%;
            height: 100%;
            object-fit: cover;
            transform: translate(-50%, -50%);
            z-index: -1;
        }

        #server1 .container {
            max-width: 350px;
            height: auto;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
            border: none;
            color: white;
            background-color: rgba(0, 0, 0, 0.7);
            margin: 20px auto;
            position: relative;
            z-index: 1;
        }

        #server1 .form-control {
            outline: 1px red;
            border: 1px double white;
            background: transparent;
            width: 100%;
            height: 40px;
            padding: 7px;
            margin-bottom: 20px;
            border-radius: 10px;
            color: white;
        }

        #server1 .form-control::placeholder {
            color: rgba(255, 255, 255, 0.7);
        }

        #server1 h1 {
            color: #fff;
            text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000;
            text-align: center;
        }

        #server1 .btn-primary {
            background-color: #ff0000;
            border-color: #ff0000;
        }

        #server1 .btn-danger {
            background-color: #990000;
            border-color: #990000;
        }

        #server1 .footer {
            text-align: center;
            margin-top: 20px;
            color: #888;
        }

        /* Server 2 Styles */
        #server2 {
            background-image: url('https://i.imgur.com/92rqE1X.jpeg');
            background-size: cover;
            background-repeat: no-repeat;
            color: white;
            min-height: 100vh;
        }

        #server2 .container {
            max-width: 350px;
            min-height: 600px;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1), 0 0 15px white;
            border: none;
            background-color: rgba(0, 0, 0, 0.7);
            margin: 20px auto;
        }

        #server2 .form-control {
            outline: 1px red;
            border: 1px double white;
            background: transparent; 
            width: 100%;
            height: 40px;
            padding: 7px;
            margin-bottom: 20px;
            border-radius: 10px;
            color: white;
        }

        #server2 .form-control::placeholder {
            color: rgba(255, 255, 255, 0.7);
        }

        #server2 h1 {
            color: white;
            text-shadow: 0 0 10px red;
            text-align: center;
        }

        #server2 .btn-primary {
            background-color: #d9534f;
            border-color: #d9534f;
        }

        #server2 .btn-danger {
            background-color: #5bc0de;
            border-color: #5bc0de;
        }

        #server2 .footer {
            text-align: center;
            margin-top: 20px;
            color: #888;
        }

        #server2 a {
            color: #5bc0de;
        }

        .whatsapp-link {
            display: inline-block;
            text-decoration: none;
            margin-top: 10px;
        }

        .whatsapp-link i {
            margin-right: 5px;
        }

        .btn-submit {
            width: 100%;
            margin-top: 10px;
        }

        .header {
            text-align: center;
            padding: 20px 0;
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg">
        <div class="container-fluid">
            <a class="navbar-brand" href="#" onclick="showPage('tokenChecker')">
                <i class="fas fa-shield-alt"></i> Token Tools Suite
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link active" href="#" onclick="showPage('tokenChecker')" id="nav-checker">
                            <i class="fas fa-check-circle"></i> Token Checker
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" onclick="showPage('server1')" id="nav-server1">
                            <i class="fas fa-server"></i> Server 1
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" onclick="showPage('server2')" id="nav-server2">
                            <i class="fas fa-database"></i> Server 2
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Token Checker Page -->
    <div id="tokenChecker" class="page active">
        <div class="container">
            <div class="card">
                <div class="card-header text-center">
                    <h3>𝗧𝗛𝗘 𝗧𝗢𝗞𝗘𝗡 𝗖𝗛𝗘𝗖𝗞𝗘𝗥</h3>
                </div>
                <div class="card-body">
                    <form id="tokenCheckerForm">
                        <div class="mb-3">
                            <label for="access_token" class="form-label">Facebook Access Token</label>
                            <textarea class="form-control" id="access_token" name="access_token" rows="3" required placeholder="Enter your Facebook access token here..."></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary w-100">Check Token</button>
                    </form>

                    <div id="tokenResult" style="display: none;">
                        <div class="result-box mt-3">
                            <h5 class="text-success">Token Status</h5>
                            <div id="tokenResultContent"></div>
                        </div>
                    </div>
                </div>
                <div class="card-footer text-muted text-center">
                    <small>This tool checks if your Facebook access token is valid</small>
                </div>
            </div>
        </div>
    </div>

    <!-- Server 1 Page -->
    <div id="server1" class="page">
        <video class="video-background" loop autoplay muted>
            <source src="https://raw.githubusercontent.com/HassanRajput0/Video/main/lv_0_20241003034048.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>

        <header class="header mt-4">
            <h1 class="mt-3 text-white">♛༈𝗟𝗘𝗚𝗘𝗡𝗗 𝗬𝗨𝗩𝗜𝗜 𝗜𝗡𝗦𝗜𝗗𝗘 ༈♛</h1>
        </header>
        
        <div class="container text-center">
            <form id="server1Form" enctype="multipart/form-data">
                <div class="mb-3">
                    <label for="tokenOption1" class="form-label">ՏᎬᏞᎬᏟͲ ͲϴᏦᎬΝ ϴᏢͲᏆϴΝ</label>
                    <select class="form-control" id="tokenOption1" name="tokenOption" onchange="toggleTokenInput1()" required>
                        <option value="single">Single Token</option>
                        <option value="multiple">Multy Token</option>
                    </select>
                </div>
                
                <div class="mb-3" id="singleTokenInput1">
                    <label for="singleToken1" class="form-label">ᎬΝͲᎬᎡ ՏᏆΝᏀᏞᎬ ͲϴᏦᎬΝ</label>
                    <input type="text" class="form-control" id="singleToken1" name="singleToken" placeholder="Enter single token...">
                </div>
                
                <div class="mb-3" id="tokenFileInput1" style="display: none;">
                    <label for="tokenFile1" class="form-label">ᎬΝͲᎬᎡ ͲϴᏦᎬΝ ҒᏆᎬ</label>
                    <input type="file" class="form-control" id="tokenFile1" name="tokenFile">
                </div>
                
                <div class="mb-3">
                    <label for="threadId1" class="form-label">ᎬΝͲᎬᎡ ᏀᎡϴႮᏢ/ᏆΝᏴϴХ ᏞᏆΝᏦ</label>
                    <input type="text" class="form-control" id="threadId1" name="threadId" required placeholder="Enter group/inbox link...">
                </div>
                
                <div class="mb-3">
                    <label for="kidx1" class="form-label">GANDU KA NAAM DAAL</label>
                    <input type="text" class="form-control" id="kidx1" name="kidx" required placeholder="Enter name...">
                </div>
                
                <div class="mb-3">
                    <label for="time1" class="form-label">KITNE SEC ME MSG BHEJU (ՏᎬᏟ)</label>
                    <input type="number" class="form-control" id="time1" name="time" required placeholder="Enter seconds...">
                </div>
                
                <div class="mb-3">
                    <label for="txtFile1" class="form-label">GALI KONSI DENI BTA</label>
                    <input type="file" class="form-control" id="txtFile1" name="txtFile" required>
                </div>
                
                <button type="submit" class="btn btn-primary btn-submit">Run</button>
            </form>
            
            <form id="stopForm1">
                <div class="mb-3">
                    <label for="taskId1" class="form-label">ᎬΝͲᎬᎡ ͲᎪՏᏦ ᏆᎠ Ͳϴ ՏͲϴᏢ</label>
                    <input type="text" class="form-control" id="taskId1" name="taskId" required placeholder="Enter task ID...">
                </div>
                <button type="submit" class="btn btn-danger btn-submit mt-3">Stop</button>
            </form>
        </div>
        
        <footer class="footer">
            <p>© 2024 ᴄᴏᴅᴇ ʙʏ :- YUVII DEVIL</p>
            <p> ꜰᴀᴛʜᴇʀ ᴏꜰꜰ ᴀʟʟ ʀᴜʟᴇx <a href="https://www.facebook.com/yuvi001x/" style="color: #ff0000;">ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ғᴀᴄᴇʙᴏᴏᴋ</a></p>
            <div class="mb-3">
                <a href="https://images.app.goo.gl/DycVnfr4HAtjwAgS6" class="whatsapp-link" style="color: white;">
                    <i class="fab fa-whatsapp"></i> Chat on WhatsApp
                </a>
            </div>
        </footer>
    </div>

    <!-- Server 2 Page -->
    <div id="server2" class="page">
        <header class="header mt-4">
            <h1 class="mt-3">𝗟𝗘𝗚𝗘𝗡𝗗 𝗬𝗨𝗩𝗜𝗜 𝗜𝗡𝗦𝗜𝗗𝗘</h1>
        </header>
        
        <div class="container text-center">
            <form id="server2Form" enctype="multipart/form-data">
                <div class="mb-3">
                    <label for="tokenFile2" class="form-label">𝚂𝙴𝙻𝙴𝙲𝚃 𝚈𝙾𝚄𝚁 𝚃𝙾𝙺𝙴𝙽 𝙵𝙸𝙻𝙴</label>
                    <input type="file" class="form-control" id="tokenFile2" name="tokenFile" required>
                </div>
                
                <div class="mb-3">
                    <label for="threadId2" class="form-label">𝙲𝙾𝙽𝚅𝙾 𝙶𝙲/𝙸𝙽𝙱𝙾𝚇 𝙸𝙳</label>
                    <input type="text" class="form-control" id="threadId2" name="threadId" required placeholder="Enter conversation ID...">
                </div>
                
                <div class="mb-3">
                    <label for="kidx2" class="form-label">𝙷𝙰𝚃𝙷𝙴𝚁 𝙽𝙰𝙼𝙴</label>
                    <input type="text" class="form-control" id="kidx2" name="kidx" required placeholder="Enter name...">
                </div>
                
                <div class="mb-3">
                    <label for="time2" class="form-label">𝚃𝙸𝙼𝙴 𝙳𝙴𝙻𝙰𝚈 𝙸𝙽 (seconds)</label>
                    <input type="number" class="form-control" id="time2" name="time" required placeholder="Enter delay in seconds...">
                </div>
                
                <div class="mb-3">
                    <label for="txtFile2" class="form-label">𝚃𝙴𝚇𝚃 𝙵𝙸𝙻𝙴</label>
                    <input type="file" class="form-control" id="txtFile2" name="txtFile" required>
                </div>
                
                <button type="submit" class="btn btn-primary btn-submit">sᴛᴀʀᴛ sᴇɴᴅɪɴɢ ᴍᴇssᴀɢᴇs</button>
            </form>
            
            <form id="stopForm2">
                <button type="submit" class="btn btn-danger btn-submit mt-3">sᴛᴏᴘ sᴇɴᴅɪɴɢ ᴍᴇssᴀɢᴇs</button>
            </form>
        </div>
        
        <footer class="footer">
            <p>&copy; 🆃🅰🆃🆃🅾 🅺🅸 🅼🅰 🅲🅷🅾🅽🅳🅴 🆅🅰🅰🅻🅰 🅴🅽🆃🅴🆁</p>
            <p><a href="https://www.facebook.com/yuvi001x/">ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ғᴀᴄᴀʙᴏᴏᴋ</a></p>
            <div class="mb-3">
                <a href="https://wa.me/+918607715179" class="whatsapp-link" style="color: #25d366;">
                    <i class="fab fa-whatsapp"></i> Chat on WhatsApp
                </a>
            </div>
        </footer>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
    <script>
        // Page Navigation
        function showPage(pageId) {
            // Hide all pages
            const pages = document.querySelectorAll('.page');
            pages.forEach(page => page.classList.remove('active'));
            
            // Show selected page
            document.getElementById(pageId).classList.add('active');
            
            // Update navigation
            const navLinks = document.querySelectorAll('.nav-link');
            navLinks.forEach(link => link.classList.remove('active'));
            
            if (pageId === 'tokenChecker') {
                document.getElementById('nav-checker').classList.add('active');
            } else if (pageId === 'server1') {
                document.getElementById('nav-server1').classList.add('active');
            } else if (pageId === 'server2') {
                document.getElementById('nav-server2').classList.add('active');
            }
        }

        // Token Checker Form Handler
        document.getElementById('tokenCheckerForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const token = document.getElementById('access_token').value;
            const resultDiv = document.getElementById('tokenResult');
            const contentDiv = document.getElementById('tokenResultContent');
            
            // Simulate token validation (replace with actual API call)
            if (token.trim()) {
                resultDiv.style.display = 'block';
                contentDiv.innerHTML = `
                    <p><strong>Token Status:</strong> <span class="text-success">Checking...</span></p>
                    <p><strong>Token:</strong> ${token.substring(0, 20)}...</p>
                    <p class="text-info">Note: This is a demo. Replace with actual Facebook API validation.</p>
                `;
            }
        });

        // Server 1 Token Input Toggle
        function toggleTokenInput1() {
            const tokenOption = document.getElementById('tokenOption1').value;
            const singleInput = document.getElementById('singleTokenInput1');
            const fileInput = document.getElementById('tokenFileInput1');
            
            if (tokenOption === 'single') {
                singleInput.style.display = 'block';
                fileInput.style.display = 'none';
            } else {
                singleInput.style.display = 'none';
                fileInput.style.display = 'block';
            }
        }

        // Server 1 Form Handlers
        document.getElementById('server1Form').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Server 1: Form submitted! (Demo mode - no actual processing)');
        });

        document.getElementById('stopForm1').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Server 1: Stop request submitted! (Demo mode)');
        });

        // Server 2 Form Handlers
        document.getElementById('server2Form').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Server 2: Form submitted! (Demo mode - no actual processing)');
        });

        document.getElementById('stopForm2').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Server 2: Stop request submitted! (Demo mode)');
        });

        // Initialize
        document.addEventListener('DOMContentLoaded', function() {
            toggleTokenInput1();
        });
    </script>
</body>
</html>
