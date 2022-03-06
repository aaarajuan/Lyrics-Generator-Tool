import os
os.system('cls' if os.name == 'nt' else 'clear')
# import module
import codecs

# open html file
f = open('output.html', 'w')

# Colors
color_off = "\033[0m"       # Text Reset
bpurple = "\033[1;35m"      # Purple
bgreen = "\033[1;32m"       # Green
bcyan = "\033[1;36m"        # Cyan
bred = "\33[91m"            # Red
blink = "\33[5m"            # Blink

print("\n"+bgreen+"Presenting...")
print(bcyan+'''                                                                                                                         
 █░░ █▄█ █▀█ █ █▀▀ █▀ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀
 █▄▄ ░█░ █▀▄ █ █▄▄ ▄█ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ ▄█
      ''')
print(bpurple+'''~ By: ██▓▒­░⡷⠂@𝚊𝚊𝚊𝚛𝚊𝚓𝚞𝚊𝚗⠐⢾░▒▓██\n''')

s_IMG = input(bcyan+'--> (Enter Song Image Url) '+bpurple+'\nroot@aaarajuan:~ '+bcyan)
s_NAME = input(bcyan+'--> (Enter Song Name) '+bpurple+'\nroot@aaarajuan:~ '+bcyan)
s_Singer = input(bcyan+'--> (Enter Song Singer Name) '+bpurple+'\nroot@aaarajuan:~ '+bcyan)
s_Composer = input(bcyan+'--> (Enter Song Composer Name) '+bpurple+'\nroot@aaarajuan:~ '+bcyan)
s_YTURL = input(bcyan+'--> (Enter Song Youtube URL ID) '+bpurple+'\nroot@aaarajuan:~ '+bcyan)
s_Artist = input(bcyan+'--> (Enter Song Artist Names) '+bpurple+'\nroot@aaarajuan:~ '+bcyan)
s_Artist_URL = input(bcyan+'--> (Enter Song Artist Tag) '+bpurple+'\nroot@aaarajuan:~ '+bcyan)
s_Direct_GD_Link = input(bcyan+'--> (Enter Song Google Drive Direct Link [MP3]) '+bpurple+'\nroot@aaarajuan:~ '+bcyan)
s_Download_Link = input(bcyan+'--> (Enter Song Download URL [MP3]): '+bpurple+'\nroot@aaarajuan:~ '+bcyan)
s_Alternative_Download_Link = input(bcyan+'--> (Enter Song Alternative Download URL [MP3]): '+bpurple+'\nroot@aaarajuan:~ '+bcyan)

code = input(bcyan+'--> (Enter Your PIN To Get The Code) '+bpurple+'\nroot@aaarajuan:~ '+bcyan)
fcode = int(code)

output = '''
<h2>
  <p>
    <span style="color: #ffa400;"><u style="background-color: white;">'''+s_NAME+''' Song Info:</u></span>
  </p>
</h2>
<hr/>
<noscript>
<div class="separator" style="clear: both; text-align: center;"><a href="'''+s_IMG+'''" style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="1371" data-original-width="2048" src="'''+s_IMG+'''" width="320" /></a></div>
</noscript>
<hr/>
<table id="song-info">
  <tbody><tr>
  </tr>
  <tr>
    <td><b>Song Name</b></td>
    <td>'''+s_NAME+'''</td>
  </tr>
  <tr>
    <td><b>Song Singer</b></td>
    <td>'''+s_Singer+'''</td>
  </tr>
  <tr>
    <td><b>Song Composer</b></td>
    <td>'''+s_Composer+'''</td>
  </tr>
  <tr>
    <td><b>Song Artist</b></td>
    <td><a href='/search/label/'''+s_Artist_URL+'''?max-results=10' target='_blank'>'''+s_Artist+'''</a></td>
  </tr>
</tbody></table>
<br />
<hr/>
<!--image: https://blogger.googleusercontent.com/img/a/AVvXsEiPVtzZIm1kZ8y5Fu86GY6H0G3uCahJuwL-VfX1lLlry9-7fcvRREltTzXCdPAJx1sjtdFniWwf713AfyDxz2uKRJDlEMVljcgDLb5YViu4jBuWKR7u2l83ubOu7CgRLsxE5EtG9CLXJGfSlf770W6cQhUxIb4yqGCzvYblb_n-G4WCJgLfXpl59nE0og=s96-->
<div class="HTML_Audio_player">
  <div class="Audio_Player_image">
    <img src="https://blogger.googleusercontent.com/img/a/AVvXsEiPVtzZIm1kZ8y5Fu86GY6H0G3uCahJuwL-VfX1lLlry9-7fcvRREltTzXCdPAJx1sjtdFniWwf713AfyDxz2uKRJDlEMVljcgDLb5YViu4jBuWKR7u2l83ubOu7CgRLsxE5EtG9CLXJGfSlf770W6cQhUxIb4yqGCzvYblb_n-G4WCJgLfXpl59nE0og=s96" style="border-radius: 60px;" />
  </div>
  <div class="player-content">
    <div class="player-info">
      <a class="song-name" href="https://youtu.be/'''+s_YTURL+'''" target="_blank">'''+s_NAME+'''</a>
      <a class="artist" href="/search/label/'''+s_Artist_URL+'''?max-results=10" target='_blank'>'''+s_Artist+'''</a>
    </div>
    <div class="k2_audio_player">
      <audio controls="" style="width: 80%;">
        <source src="'''+s_Direct_GD_Link+'''" type="audio/mpeg"/>
      </audio>
    </div>
  </div>
</div>
<br /><br /><br />
<h2>
  <p>
    <span style="color: #ffa400;"><u>'''+s_NAME+''' Song Lyrics:</u></span>
  </p>
</h2>
<div style="width: 100%;">
  <div class="tabs-container">
    <div class="tabs">
      <div class="tab active">English</div>
      <div class="tab">Hindi</div>
    </div>
    <div class="content-container">
      <div class="content active">
        <h3>'''+s_NAME+''' Song Lyrics - English</h3>
        <p>
          Lyrics Here Lyrics Here Lyrics Here Lyrics Here Lyrics Here Lyrics
          Here Lyrics Here
        </p>
      </div>

      <div class="content">
        <h3>'''+s_NAME+''' Song Lyrics - Hindi</h3>

        <p>
          Lyrics Here Lyrics Here Lyrics Here Lyrics Here Lyrics Here Lyrics
          Here Lyrics Here
        </p>
      </div>
    </div>
  </div>
</div>
<h2>
  <span style="color: #ffa400;"><u><span>'''+s_NAME+''' Lyrics Watch Video Song:</span><span></span></u></span>
</h2>
<p>
  <iframe class="lazyload" title="Youtube"
  width="400" height="300" allowfullscreen
  allow="accelerometer;autoplay;encrypted-media;gyroscope;picture-in-picture"
  data-style="background: url(https://img.youtube.com/vi/'''+s_YTURL+'''/hqdefault.jpg) 50% 50% / cover no-repeat;"
  data-src="https://www.youtube.com/embed/'''+s_YTURL+'''?autoplay=0&origin=https://www.freefilescr.com"></iframe>
</p>

<h2>
  <p>
    <span style="color: #ffa400;"><u>'''+s_NAME+''' Song Download (Audio):</u></span>
  </p>
</h2>
<p>All Download Links is a DIrect Download Link.</p>
<div style="border-radius: 2px; border: 5px solid skyblue;">
  <ul>
    <!--Download Link-->
    <center>
      <!--paste ads code here-->
    </center>
    <br />
    <p style="margin: 0px;">
      <!--text here-->
      <b>Download The Song (Audio Only) =&gt; </b><em>'''+s_NAME+'''.mp3</em>
    </p>
    <br />
    <form action="/p/download.html" style="margin-bottom: 15px;" target="_blank">
      <button id="redirect-download" onclick="redirectbtn();">
        <i class="fa fa-download"></i> Download
      </button>
    </form>
    <center>
      <!--paste ads code here-->
    </center>
    <script>
      // download link paste here
         var link = "'''+s_Download_Link+'''";
    </script>

    <center>
      <!--paste ads code here-->
    </center>
    <p style="margin: 0px;">
      <!--text here-->
      <span id="post-Title"></span>
    </p>
    <form action="/p/download.html" style="margin-bottom: 15px;" target="_blank">
      <button id="redirect-download" onclick="redirectbtn();">
        <i class="fa fa-download"></i>Alternative Download
      </button>
    </form>
    <center>
      <!--paste ads code here-->
    </center>
    <script>
      // download link paste here
         var link = "'''+s_Alternative_Download_Link+'''";
    </script>
  </ul>
</div>
<div id="gtx-trans" style="left: 57px; position: absolute; top: 612.875px;"><div class="gtx-trans-icon"></div></div>
<hr/>
<table id="more-songs">
  <tbody><tr>
    <th>
      <center><span style="color: #ffa400;"><u>- More Lyrics -</u></span></center>
    </th>
  </tr>
  <tr>
    <td><center>Song Name</center></td>
  </tr>
  <tr>
    <td><center>Song Artist</center></td>
  </tr>
</tbody>
</table>
        '''

# writing the code into the file
f.write(output)

# close the file
f.close()

#output
if fcode == 9109:
  print('''\n'''+bgreen+blink+'''Generating Your Code Please Wait...\n'''+color_off+bred+output)
else:
  print('Ops There is a Problem In Our End Please Try Again!')
  
# viewing html files
# below code creates a 
# codecs.StreamReaderWriter object
file = codecs.open("output.html", 'r', "utf-8")

# using .read method to view the html 
# code from our object
print(file.read())

