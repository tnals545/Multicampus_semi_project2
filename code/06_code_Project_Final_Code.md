# Project Final Code

> colab 가상환경에서 사용한 코드입니다.



### 사전 준비

```python
# 라이브러리 설치
!pip install fastapi nest_asyncio pyngrok uvicorn aiofiles python-multipart
```

```python
# ngrok key 사용
!ngrok authtoken **
```

```python
# 파일 생성
!mkdir templates
!mkdir static
```



---



### HTML

```css
# main page-css

%%writefile static/main2.css
@import url(https://fonts.googleapis.com/css?family=Roboto:400,700,500);

/* main Styles */

html { box-sizing: border-box; }

*, *:before, *:after { box-sizing: inherit; }

body {
    background: #fafafa;
    font-family: "Roboto", sans-serif;
    font-size: 14px;
    margin: 0;
}

a { text-decoration: none; }

.container {
    width: 1000px;
    margin: auto;
}

h1 { text-align:center; margin-top:100px;}

/* Navigation Styles */

/* nav { background: #2ba0db; } */

nav ul {
    font-size: 0;
    margin: 0;
    padding: 0;
}

nav ul li {
    display: inline-block;
    position: relative;
}

nav ul li a {
    color: #212121;
    display: block;
    font-size: 14px;
    padding: 15px 14px;
    transition: 0.3s linear;
}

nav ul li:hover {
  background: rgba( 255, 0, 0, 0.8 );
}

nav ul li ul {
    border-bottom: 5px solid rgba( 255, 0, 0, 0.8 );
    display: none;
    position: absolute;
    width: 250px;
}

nav ul li ul li {
    border-top: 1px solid #444;
    display: block;
}

nav ul li ul li:first-child { border-top: none; }

nav ul li ul li a {
    background: #fff;
    display: block;
    padding: 10px 14px;
}

nav ul li ul li a:hover { background: rgba( 255, 100, 100 ); }

nav .fa.fa-angle-down { margin-left: 6px; }

#wrap nav {
  float: right;
}

header {
  padding: 50px 50px;
  text-align:center;
}
```

```css
# 나머지-css

%%writefile static/style.css
.input-file-button{
  padding: 6px 26px;
  border-radius: 8px;
  color: black;
  cursor: pointer;
  margin-left: 180px;
  border: solid black;
}

.input-submit-button{
  padding: 12px 52px;
  border-radius: 8px;
  border: rgba( 255, 0, 0, 0.8 );
  background-color: rgba( 255, 0, 0, 0.8 );
  color: white;
  cursor: pointer;
  font-size:20px;
}

input::file-selector-button {
  display:none;
}

.input_center {
  text-align: center;
}

#input-file{
  margin: 15px
}

#input-submit {
  display:none;
}

table {
  width: 300px;
  border: 1px solid #000000;
  border-collapse: collapse;
}

table td {
  border: 1px solid #fe7e48;
  padding: 0px 20px;
}

table.hidden {
  border-style: hidden;
  margin: 10px;
}

.center {
  text-align: center;
}

.copy {
  border: 2px solid black;
  margin: auto;
  width: 500px;
  text-align: center;

}
```

```html
# 메인 페이지

%%writefile templates/main2.html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Junior Naver</title>
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/4.6.2/css/font-awesome.min.css">
    <link rel="stylesheet" href= "{{ url_for('static', path='/main2.css') }}">
</head>
<body>
  <div id="wrap">
  <nav>
    <ul class="nav-items">
      <li><a href="#home">Sign up</a></li>
      <li><a href="#news">Login</a></li>
      <li><a href="#contact">Service center</a></li>
    </ul>
  </nav>
  <header>
    <a class='logo' href="/"><img src= "{{ url_for('static', path='/logo.png') }}" height="150px"></a>
  </header>
  </div>

  <nav>
      <div class="container">
          <ul>
              <li> <a href="#">Script<i class='fa fa-angle-down'></i></a>
                  <ul>
                      <li><a href="/speech_text">Script text</a></li>
                      <li><a href="/speech_translation">Script Translation</a></li>
                      <li><a href="/speech_voice">Script Voice</a></li>
                  </ul>
              </li>
              <li><a href="/eye">Eye Detector</a></li>
              <li><a href="/face">Face Detector</a></li>
          </ul>
      </div>
  </nav>


  <a href='/speech_text'><img src="{{ url_for('static', path='/smart.png') }}"width="100%"></a>
  <a href='/eye'><img src="{{ url_for('static', path='/sleep.png') }}" width="100%"></a>
  <a href='/face'><img src="{{ url_for('static', path='/age.png') }}"  width="100%"></a>

  <script src="http://code.jquery.com/jquery-1.12.4.min.js"></script>
  <script>
      $('nav li').hover(
          function() {
              $('ul', this).stop().slideDown(200);
          },
          function() {
              $('ul', this).stop().slideUp(200);
          }
      );
  </script>


</body>
</html>
```

```html
# 스크립트 텍스트업로드

%%writefile templates/speech_text.html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Smart_Text</title>
  <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/4.6.2/css/font-awesome.min.css">
  <link rel="stylesheet" href= "{{ url_for('static', path='/main2.css') }}">
  <link rel="stylesheet" href= "{{ url_for('static', path='/style.css') }}">
</head>
<body>
  <div id="wrap">
  <nav>
    <ul class="nav-items">
      <li><a href="#home">Sign up</a></li>
      <li><a href="#news">Login</a></li>
      <li><a href="#contact">Service center</a></li>
    </ul>
  </nav>
  <header>
    <a class='logo' href="/"><img src= "{{ url_for('static', path='/logo.png') }}" height="150px"></a>
  </header>
  </div>

  <nav>
      <div class="container">
          <ul>
              <li> <a href="#">Smart Script<i class='fa fa-angle-down'></i></a>
                  <ul>
                      <li><a href="/speech_text">Smart Text</a></li>
                      <li><a href="/speech_translation">Smart Translation</a></li>
                      <li><a href="/speech_voice">Smart Voice</a></li>
                  </ul>
              </li>
              <li><a href="/eye">Eye Detector</a></li>
              <li><a href="/face">Face Detector</a></li>
          </ul>
      </div>
    <script src="http://code.jquery.com/jquery-1.12.4.min.js"></script>
    <script>
      $('nav li').hover(
          function() {
              $('ul', this).stop().slideDown(200);
          },
          function() {
              $('ul', this).stop().slideUp(200);
          }
      );
    </script>
  </nav>

  <h1>Smart Text</h1>
  <div class="input_center">
    <p>이 앱은 비디오 파일의 스크립트를 추출하기에 유용합니다.<br> 이 앱은 설치가 필요하지 않고 브라우저에서 작동합니다.</p>
    <br>
    <br>
    <form action="/speech/text" method="post" enctype="multipart/form-data">
      <label class="input-file-button" for="input-file" style="font-size:15px;">
        업로드
      </label>
      <input type="file" id="input-file" name="files" style="font-size:15px;">
      <br>
      <br>
      <br>

      <label class="input-submit-button" for="input-submit">
        Submit
      </label>
      <input type="submit" id="input-submit">
    </form>
  </div>


</body>
</html>
```

```html
# 스크립트 텍스트 결과

%%writefile templates/speech_text_result.html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Smart_Text_result</title>
  <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/4.6.2/css/font-awesome.min.css">
  <link rel="stylesheet" href= "{{ url_for('static', path='/main2.css') }}">
  <link rel="stylesheet" href= "{{ url_for('static', path='/style.css') }}">
</head>
<body>
  <div id="wrap">
  <nav>
    <ul class="nav-items">
      <li><a href="#home">Sign up</a></li>
      <li><a href="#news">Login</a></li>
      <li><a href="#contact">Service center</a></li>
    </ul>
  </nav>
  <header>
    <a class='logo' href="/"><img src= "{{ url_for('static', path='/logo.png') }}" height="150px"></a>
  </header>
  </div>

  <nav>
      <div class="container">
          <ul>
              <li> <a href="#">Smart Script<i class='fa fa-angle-down'></i></a>
                  <ul>
                      <li><a href="/speech_text">Smart Text</a></li>
                      <li><a href="/speech_translation">Smart Translation</a></li>
                      <li><a href="/speech_voice">Smart Voice</a></li>
                  </ul>
              </li>
              <li><a href="/eye">Eye Detector</a></li>
              <li><a href="/face">Face Detector</a></li>
          </ul>
      </div>
    <script src="http://code.jquery.com/jquery-1.12.4.min.js"></script>
    <script>
      $('nav li').hover(
          function() {
              $('ul', this).stop().slideDown(200);
          },
          function() {
              $('ul', this).stop().slideUp(200);
          }
      );
  </script>
  </nav>

  <h1>Smart Text</h1>
  <div class="input_center">
    <p>이 앱은 비디오 파일의 스크립트를 추출하기에 유용합니다.<br> 이 앱은 설치가 필요하지 않고 브라우저에서 작동합니다.</p>
    <br>
    <br>
    <h2>변환 내용입니다.</h2>
    <div class='copy'>
      <p id="text1">{{result}}</p>
    </div><br>
      <button class=input-submit-button onclick="copyToClipboard('text1')">Copy</button>
    </div>


  <script>
       function copyToClipboard(elementId) {
    var aux = document.createElement("input");
    aux.setAttribute("value", document.getElementById(elementId).innerHTML);
    document.body.appendChild(aux);

    aux.select();
    document.execCommand("copy");
    document.body.removeChild(aux);
    }
  </script>


</body>
</html>
```

```html
# 스크립트 번역 업로드

%%writefile templates/speech_translation.html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Smart_Translation</title>
  <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/4.6.2/css/font-awesome.min.css">
  <link rel="stylesheet" href="{{ url_for('static', path='/main2.css') }}">
  <link rel="stylesheet" href="{{ url_for('static', path='/style.css') }}">
</head>
<body>

  <div id="wrap">
  <nav>
    <ul class="nav-items">
      <li><a href="#home">Sign up</a></li>
      <li><a href="#news">Login</a></li>
      <li><a href="#contact">Service center</a></li>
    </ul>
  </nav>
  <header>
    <a class='logo' href="/"><img src= "{{ url_for('static', path='/logo.png') }}" height="150px"></a>
  </header>
  </div>

  <nav>
      <div class="container">
          <ul>
              <li> <a href="#">Smart Script<i class='fa fa-angle-down'></i></a>
                  <ul>
                      <li><a href="/speech_text">Smart Text</a></li>
                      <li><a href="/speech_translation">Smart Translation</a></li>
                      <li><a href="/speech_voice">Smart Voice</a></li>
                  </ul>
              </li>
              <li><a href="/eye">Eye Detector</a></li>
              <li><a href="/face">Face Detector</a></li>
          </ul>
      </div>
    <script src="http://code.jquery.com/jquery-1.12.4.min.js"></script>
    <script>
      $('nav li').hover(
          function() {
              $('ul', this).stop().slideDown(200);
          },
          function() {
              $('ul', this).stop().slideUp(200);
          }
      );
    </script>
  </nav>

  <h1>Smart Translation</h1>
  <div class="input_center">
    <p>이 앱은 비디오 파일의 번역 스크립트를 추출하기에 유용합니다.<br>이 앱은 설치가 필요하지 않고 브라우저에서 작동합니다.</p>
    <br>
    <form action="/speech/translation" method="post" enctype="multipart/form-data">
    
      <label for="source">원본 언어 ( EN, KR ):</label>
      <select name = "source">
        <option value = "en">영어</option>
        <option value = "ko">한국어</option>
      </select>
      <br>
      <br>
      <label for="target">번역 언어 ( EN, KR, JP ):</label>
      <select name = "target">
        <option value = "en">영어</option>
        <option value = "ko">한국어</option>
        <option value = "ja">일본어</option>
      </select>
    <br>
    <br>
      <label class="input-file-button" for="input-file" style="font-size:15px;">
        업로드
      </label>
      <input type="file" id="input-file" name="files" style="font-size:15px;">
      <br>
      <br>
      <br>

      <label class="input-submit-button" for="input-submit">
        Submit
      </label>
      <input type="submit" id="input-submit">
    </form>
  </div>

  
</body>
</html>
```

```html
# 스크립트 번역 결과

%%writefile templates/speech_translation_result.html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Smart_Translation_result</title>
  <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/4.6.2/css/font-awesome.min.css">
  <link rel="stylesheet" href="{{ url_for('static', path='/main2.css') }}">
  <link rel="stylesheet" href="{{ url_for('static', path='/style.css') }}">
</head>
<body>
  <div id="wrap">
  <nav>
    <ul class="nav-items">
      <li><a href="#home">Sign up</a></li>
      <li><a href="#news">Login</a></li>
      <li><a href="#contact">Service center</a></li>
    </ul>
  </nav>
  <header>
    <a class='logo' href="/"><img src= "{{ url_for('static', path='/logo.png') }}" height="150px"></a>
  </header>
  </div>

  <nav>
      <div class="container">
          <ul>
              <li> <a href="#">Smart Script<i class='fa fa-angle-down'></i></a>
                  <ul>
                      <li><a href="/speech_text">Smart Text</a></li>
                      <li><a href="/speech_translation">Smart Translation</a></li>
                      <li><a href="/speech_voice">Smart Voice</a></li>
                  </ul>
              </li>
              <li><a href="/eye">Eye Detector</a></li>
              <li><a href="/face">Face Detector</a></li>
          </ul>
      </div>
    <script src="http://code.jquery.com/jquery-1.12.4.min.js"></script>
    <script>
      $('nav li').hover(
          function() {
              $('ul', this).stop().slideDown(200);
          },
          function() {
              $('ul', this).stop().slideUp(200);
          }
      );
    </script>
  </nav>

  <h1>Smart Translation</h1>
  <div class="input_center">
    <p>이 앱은 비디오 파일의 번역 스크립트를 추출하기에 유용합니다.<br>이 앱은 설치가 필요하지 않고 브라우저에서 작동합니다.</p>
    <br>
    <br>
    <br><br>
    <h2>변환 내용입니다.</h2>
    <div class='copy'>
      <!--복사할 텍스트 만들기-->
      <p id="text1">{{trans}}</p>
    </div><br>
      <button class=input-submit-button onclick="copyToClipboard('text1')">Copy</button>
    </div>

  <!--// 버튼 만들기-->

  <script>
    // 클립보드로 복사하는 기능을 생성
    function copyToClipboard(elementId) {
      // 글을 쓸 수 있는 란을 만든다.
    var aux = document.createElement("input");
      // 지정된 요소의 값을 할당 한다.
    aux.setAttribute("value", document.getElementById(elementId).innerHTML);
      // bdy에 추가한다.
    document.body.appendChild(aux);
      // 지정된 내용을 강조한다.
    aux.select();
      // 텍스트를 카피 하는 변수를 생성
    document.execCommand("copy");
      // body 로 부터 다시 반환 한다.
    document.body.removeChild(aux);
    }
  </script>



</body>
</html>
```

```html
# 스크립트 보이스 업로드

%%writefile templates/speech_voice.html
<!DOCTYPE html>
<html>
<body>
  <meta charset="utf-8">
  <title>Smart_Voice</title>
  <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/4.6.2/css/font-awesome.min.css">
  <link rel="stylesheet" href="{{ url_for('static', path='/main2.css') }}">
  <link rel="stylesheet" href="{{ url_for('static', path='/style.css') }}">
</head>
<body>

  <div id="wrap">
  <nav>
    <ul class="nav-items">
      <li><a href="#home">Sign up</a></li>
      <li><a href="#news">Login</a></li>
      <li><a href="#contact">Service center</a></li>
    </ul>
  </nav>
  <header>
    <a class='logo' href="/"><img src= "{{ url_for('static', path='/logo.png') }}" height="150px"></a>
  </header>
  </div>

  <nav>
      <div class="container">
          <ul>
              <li> <a href="#">Smart Script<i class='fa fa-angle-down'></i></a>
                  <ul>
                      <li><a href="/speech_text">Smart Text</a></li>
                      <li><a href="/speech_translation">Smart Translation</a></li>
                      <li><a href="/speech_voice">Smart Voice</a></li>
                  </ul>
              </li>
              <li><a href="/eye">Eye Detector</a></li>
              <li><a href="/face">Face Detector</a></li>
          </ul>
      </div>
        <script src="http://code.jquery.com/jquery-1.12.4.min.js"></script>
  <script>
      $('nav li').hover(
          function() {
              $('ul', this).stop().slideDown(200);
          },
          function() {
              $('ul', this).stop().slideUp(200);
          }
      );
  </script>
  </nav>

  <h1>Smart Voice</h1>
  <div class="input_center">
    <p>파일을 업로드하고 'Submit'을 클릭하면 영어를 한국어로 번역 후 음성으로 녹음한 파일을 지원해 줍니다.<br>이 앱은 설치가 필요하지 않고 브라우저에서 작동합니다.</p>
    <br>
    <br>
    <form action="/speech/voice" method="post" enctype="multipart/form-data">
      <label class="input-file-button" for="input-file" style="font-size:15px;">
        업로드
      </label>
      <input type="file" id="input-file" name='files' style="font-size:15px;">
      <br>
      <br>
      <br>
      <label class="input-submit-button" for="input-submit">
        Submit
      </label>
      <input type="submit" id="input-submit">
    </form>
  </div>



</body>
</html>
```

```html
# 시청 제한 업로드

%%writefile templates/face.html
<!DOCTYPE html>
<html>
<body>
  <meta charset="utf-8">
  <title>Face_Detector</title>
  <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/4.6.2/css/font-awesome.min.css">
  <link rel="stylesheet" href="{{ url_for('static', path='/main2.css') }}">
  <link rel="stylesheet" href="{{ url_for('static', path='/style.css') }}">
</head>
<body>
  <div id="wrap">
  <nav>
    <ul class="nav-items">
      <li><a href="#home">Sign up</a></li>
      <li><a href="#news">Login</a></li>
      <li><a href="#contact">Service center</a></li>
    </ul>
  </nav>
  <header>
    <a class='logo' href="/"><img src= "{{ url_for('static', path='/logo.png') }}" height="150px"></a>
  </header>
  </div>

  <nav>
      <div class="container">
          <ul>
              <li> <a href="#">Smart Script<i class='fa fa-angle-down'></i></a>
                  <ul>
                      <li><a href="/speech_text">Smart Text</a></li>
                      <li><a href="/speech_translation">Smart Translation</a></li>
                      <li><a href="/speech_voice">Smart Voice</a></li>
                  </ul>
              </li>
              <li><a href="/eye">Eye Detector</a></li>
              <li><a href="/face">Face Detector</a></li>
          </ul>
      </div>
      <script src="http://code.jquery.com/jquery-1.12.4.min.js"></script>
      <script>
      $('nav li').hover(
        function() {
          $('ul', this).stop().slideDown(200);
        },
        function() {
          $('ul', this).stop().slideUp(200);
        }
      );
      </script>
  </nav>

  <h1>Face Detector</h1>
  <div class="input_center">
    <p>화면 속 인물의 나이를 판단하여 시청 가능한 연령인지 확인하고, 확인된 연령에 따라 시청 가능 영상이 제한됩니다.</p>
    <br>
    <br>
    <form action="/face/age" method="post" enctype="multipart/form-data">
      <label class="input-file-button" for="input-file" style="font-size:15px;">
        업로드
      </label>
      <input type="file" id="input-file" name='files' style="font-size:15px;">
      <br>
      <br>
      <br>
      <label class="input-submit-button" for="input-submit">
        Submit
      </label>
      <input type="submit" id="input-submit">
    </form>
    <br>
    <br>
    <br>
    <h2>연령에 따라 시청이 제한됩니다.</h2>
  </div>

</body>
</html>
```

```html
# 시청제한 결과

%%writefile templates/face_result.html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Face_Detector_result</title>
  <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/4.6.2/css/font-awesome.min.css">
  <link rel="stylesheet" href="{{ url_for('static', path='/main2.css') }}">
  <link rel="stylesheet" href="{{ url_for('static', path='/style.css') }}">
</head>
<body>
  <div id="wrap">
  <nav>
    <ul class="nav-items">
      <li><a href="#home">Sign up</a></li>
      <li><a href="#news">Login</a></li>
      <li><a href="#contact">Service center</a></li>
    </ul>
  </nav>
  <header>
    <a class='logo' href="/"><img src= "{{ url_for('static', path='/logo.png') }}" height="150px"></a>
  </header>
  </div>

  <nav>
      <div class="container">
          <ul>
              <li> <a href="#">Smart Script<i class='fa fa-angle-down'></i></a>
                  <ul>
                      <li><a href="/speech_text">Smart Text</a></li>
                      <li><a href="/speech_translation">Smart Translation</a></li>
                      <li><a href="/speech_voice">Smart Voice</a></li>
                  </ul>
              </li>
              <li><a href="/eye">Eye Detector</a></li>
              <li><a href="/face">Face Detector</a></li>
          </ul>
      </div>
      <script src="http://code.jquery.com/jquery-1.12.4.min.js"></script>
      <script>
      $('nav li').hover(
        function() {
          $('ul', this).stop().slideDown(200);
        },
        function() {
          $('ul', this).stop().slideUp(200);
        }
      );
      </script>
  </nav>

  <h1>Face Detector</h1>
  <div class="input_center">
    <p>화면 속 인물의 나이를 판단하여 시청 가능한 연령인지 확인하고, 확인된 연령에 따라 시청 가능 영상이 제한됩니다.</p>
    <br>
    <br>
    <h2>{{msg}}</h2>
  </div>


</body>
</html>
```

```html
# 미시청 인식

%%writefile templates/eye.html
<!DOCTYPE html>
<html>
<body>
  <meta charset="utf-8">
  <title>Eye_Dectector</title>
  <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/4.6.2/css/font-awesome.min.css">
  <link rel="stylesheet" href="{{ url_for('static', path='/main2.css') }}">
  <link rel="stylesheet" href="{{ url_for('static', path='/style.css') }}">
</head>
<body>
  <div id="wrap">
  <nav>
    <ul class="nav-items">
      <li><a href="#home">Sign up</a></li>
      <li><a href="#news">Login</a></li>
      <li><a href="#contact">Service center</a></li>
    </ul>
  </nav>
  <header>
    <a class='logo' href="/"><img src= "{{ url_for('static', path='/logo.png') }}" height="150px"></a>
  </header>
  </div>

  <nav>
      <div class="container">
          <ul>
              <li> <a href="#">Smart Script<i class='fa fa-angle-down'></i></a>
                  <ul>
                      <li><a href="/speech_text">Smart Text</a></li>
                      <li><a href="/speech_translation">Smart Translation</a></li>
                      <li><a href="/speech_voice">Smart Voice</a></li>
                  </ul>
              </li>
              <li><a href="/eye">Eye Detector</a></li>
              <li><a href="/face">Face Detector</a></li>
          </ul>
      </div>
      <script src="http://code.jquery.com/jquery-1.12.4.min.js"></script>
      <script>
      $('nav li').hover(
        function() {
          $('ul', this).stop().slideDown(200);
        },
        function() {
          $('ul', this).stop().slideUp(200);
        }
      );
      </script>
  </nav>

  <h1>Eye Detector</h1>
  <div class="input_center">
    <p>사용자의 눈을 인식하여 일정 시간 화면을 보고 있지 않다고 판단되면 경고 메시지를 보냅니다.<br>만약 응답이 없을 시 시청 중인 영상을 종료합니다.</p>
    <br>
    <br>
    <h2>영상을 'On' 해주시기 바랍니다.</h2><br>
    <form action="/eye/detector" method="post">
      <label class="input-submit-button" for="input-submit">
        Video On
      </label>
      <input type="submit" id="input-submit">
    </form>
  </div>


</body>
</html>
```

```html
# 미시청 인식 결과

%%writefile templates/eye_result.html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Eye_Detector_result</title>
  <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/4.6.2/css/font-awesome.min.css">
  <link rel="stylesheet" href="{{ url_for('static', path='/main2.css') }}">
  <link rel="stylesheet" href="{{ url_for('static', path='/style.css') }}">
</head>
<body>
  <div id="wrap">
  <nav>
    <ul class="nav-items">
      <li><a href="#home">Sign up</a></li>
      <li><a href="#news">Login</a></li>
      <li><a href="#contact">Service center</a></li>
    </ul>
  </nav>
  <header>
    <a class='logo' href="/"><img src= "{{ url_for('static', path='/logo.png') }}" height="150px"></a>
  </header>
  </div>

  <nav>
      <div class="container">
          <ul>
              <li> <a href="#">Smart Script<i class='fa fa-angle-down'></i></a>
                  <ul>
                      <li><a href="/speech_text">Smart Text</a></li>
                      <li><a href="/speech_translation">Smart Translation</a></li>
                      <li><a href="/speech_voice">Smart Voice</a></li>
                  </ul>
              </li>
              <li><a href="/eye">Eye Detector</a></li>
              <li><a href="/face">Face Detector</a></li>
          </ul>
      </div>
      <script src="http://code.jquery.com/jquery-1.12.4.min.js"></script>
      <script>
      $('nav li').hover(
        function() {
          $('ul', this).stop().slideDown(200);
        },
        function() {
          $('ul', this).stop().slideUp(200);
        }
      );
      </script>
  </nav>

  <h1>Eye Detector</h1>
  <div class="input_center">
    <p>사용자의 눈을 인식하여 일정 시간 화면을 보고 있지 않다고 판단되면 경고 메시지를 보냅니다.<br>만약 응답이 없을 시 시청 중인 영상을 종료합니다.</p>
    <br>
    <br>
    <video width="640" height="480" controls autoplay="autoplay" muted="muted">
      <source src={{ fn }} type="video/mp4">
      </video>
  </div>



</body>
</html>
```



---



### FastAPI

```python
# 라이브러리
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import nest_asyncio
from pyngrok import ngrok
import uvicorn
from typing import Optional, List
from fastapi import File, UploadFile
import os
import numpy as np
import urllib.request
import requests
import json
```

```python
# smart text

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount('/static', StaticFiles(directory='static'), name='static')

# 메인 홈페이지
@app.get('/', response_class=HTMLResponse)
def read_root(request: Request):
  return templates.TemplateResponse("main2.html", {"request": request})


class ClovaSpeechClient:
  # Clova Speech invoke URL
  invoke_url = 'https://clovaspeech-gw.ncloud.com/external/v1/2389/135ddb361331ff2821f583d720d636d5e9fc782ab76ece949d5ab49b83e39c85'
  # Clova Speech secret key
  secret = '523aadbce32e48d499728ffa3e9389a3'

  def req_upload(self, file, completion, callback=None, userdata=None, forbiddens=None, boostings=None,
                  wordAlignment=True, fullText=True, diarization={"enable":True}):
      request_body = {
          'language': 'enko',
          'completion': completion,
          'callback': callback,
          'userdata': userdata,
          'wordAlignment': wordAlignment,
          'fullText': fullText,
          'forbiddens': forbiddens,
          'boostings': boostings,
          'diarization': diarization
      }
      headers = {
          'Accept': 'application/json;UTF-8',
          'X-CLOVASPEECH-API-KEY': self.secret
      }
      print(json.dumps(request_body, ensure_ascii=False).encode('UTF-8'))
      files = {
          'media': open(file, 'rb'),
          'params': (None, json.dumps(request_body, ensure_ascii=False).encode('UTF-8'), 'application/json')
      }
      response = requests.post(headers=headers, url=self.invoke_url + '/recognizer/upload', files=files)
      return response

@app.get('/speech_text', response_class=HTMLResponse)
async def speech_text_file(request: Request):
  return templates.TemplateResponse("speech_text.html", {"request": request})


@app.post('/speech/text', response_class=HTMLResponse)
async def speech_text(request: Request, files: List[UploadFile] = File(...)):
  for file in files:
    contents = await file.read()
    with open(os.path.join('/content/',file.filename), 'wb') as fp:
      fp.write(contents)
    if __name__ == '__main__':

      res = ClovaSpeechClient().req_upload(file=(os.path.join('/content/' + file.filename)), completion='sync')

      a = res.json()['segments']
      result = []
    for i in range(len(a)):
      t = a[i]['textEdited']
      p = a[i]['speaker']['label']
      if t == '':
        pass
      else :
        result.append([p+':'+t])

  return templates.TemplateResponse("speech_text_result.html", {"request": request, "result":result})
```

```python
# smart translation

@app.get('/speech_translation', response_class=HTMLResponse)
async def speech_tr_file(request: Request):
  return templates.TemplateResponse("speech_translation.html", {"request": request})

@app.post('/speech/translation', response_class=HTMLResponse)
async def speech_tr(req: Request, source : str = Form(...), target : str = Form(...) ,files: List[UploadFile] = File(...)):
  for file in files:
    contents = await file.read()
    with open(os.path.join('/content/',file.filename), 'wb') as fp:
      fp.write(contents)
    if __name__ == '__main__':
      res = ClovaSpeechClient().req_upload(file=(os.path.join('/content/' + file.filename)), completion='sync')
      a = res.json()['text']

    # translation
    client_id = "is0x54abfw"
    client_secret = "zBj1LcxbrsNwc4nJdaB1jwLEtM3GEV0aPD5kL6FT"
    encText = urllib.parse.quote(a)
    data = "source=%s&target=%s&honorific=True&text="% (source, target) + encText  # 영어 한국어 설정
    url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
    request.add_header("X-NCP-APIGW-API-KEY",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()   
        #print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

    respBody = response_body.decode('utf-8') 
    respBodyDict = json.loads(respBody)
    trans = respBodyDict['message']['result']['translatedText']

  return templates.TemplateResponse("speech_translation_result.html", {'request': req, 'trans':trans})
```

```python
# smart voice

@app.get('/speech_voice', response_class=HTMLResponse)
async def speech_voice_file(request: Request):
  return templates.TemplateResponse("speech_voice.html", {"request": request})

@app.post('/speech/voice')
async def speech_voice(files: List[UploadFile] = File(...)):
  for file in files:
    contents = await file.read()
    with open(os.path.join('/content/',file.filename), 'wb') as fp:
      fp.write(contents)
    if __name__ == '__main__':
      res = ClovaSpeechClient().req_upload(file=(os.path.join('/content/' + file.filename)), completion='sync')


    result = res.json()['text']
    # translation
    client_id = "is0x54abfw"
    client_secret = "zBj1LcxbrsNwc4nJdaB1jwLEtM3GEV0aPD5kL6FT"
    encText = urllib.parse.quote(result)
    data = "source=en&target=ko&honorific=True&text=" + encText  # 영어 한국어 설정
    url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
    request.add_header("X-NCP-APIGW-API-KEY",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
        
    mas = response_body.decode('utf-8')
    translation = mas.split('"')[-2]


    # voice
    encText = urllib.parse.quote(translation)
    data = "speaker=nara&volume=0&speed=0&pitch=0&format=mp3&text=" + encText;
    url = "https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
    request.add_header("X-NCP-APIGW-API-KEY",client_secret)
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()
    if(rescode==200):
        # print("TTS mp3 저장")
        response_body = response.read()
        fn = file.filename.split('.')[0]
        with open('./static/%s_voice.mp3'% fn, 'wb') as f:
            f.write(response_body)
    else:
        print("Error Code:" + rescode)
    file_path = os.getcwd() + '/static/%s_voice.mp3'% fn
  return FileResponse(path=file_path, media_type='application/octet-stream', filename= '%s_voice.mp3'% fn)
```

```python
# 시청제한

@app.get('/face', response_class=HTMLResponse)
async def face_age(request: Request):
  return templates.TemplateResponse("face.html", {"request": request})

@app.post('/face/age', response_class=HTMLResponse)
async def face_age_result(request: Request, files: List[UploadFile] = File(...)):
  for file in files:
    contents = await file.read()
    with open(os.path.join('/content/',file.filename), 'wb') as fp:
      fp.write(contents)
      client_id = "s3etavmw8n"
      client_secret = "k4VTQDwCAm3yJMbJCYg0lqIvNAJk35glQKuMzjkp"
      url = "https://naveropenapi.apigw.ntruss.com/vision/v1/face"
      files = {'image': open(os.path.join('/content/',file.filename), 'rb')}
      headers = {'X-NCP-APIGW-API-KEY-ID': client_id, 'X-NCP-APIGW-API-KEY': client_secret }
      response = requests.post(url,  files=files, headers=headers)
      rescode = response.status_code
      if(rescode==200):
          print (response.text)
      else:
          print("Error Code:" + rescode)
      res = response.json()
      low = int(res['faces'][0]['age']['value'].split('~')[0])
      high = int(res['faces'][0]['age']['value'].split('~')[1])
      if (low + high) / 2 < 15:
        msg = "시청 불가능한 연령입니다.(15세 미만)"
      else:
        msg = "시청 가능한 연령입니다.(15세 이상)"

  return templates.TemplateResponse("face_result.html", {"request": request, "msg":msg})
```

```python
# 미시청인식

@app.get('/eye', response_class=HTMLResponse)
async def eye_detector(request: Request):
  return templates.TemplateResponse("eye.html", {"request": request})

@app.post('/eye/detector', response_class=HTMLResponse)
async def eye_detector_result(request: Request):
  return templates.TemplateResponse("eye_result.html", {"request": request, "fn": '/static/insic.mp4'})
```

```python
app.url_path_for('static', path='/insic.mp4')
```

```python
ngrok_tunnel = ngrok.connect(8000)
print('Public URL:' , ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, host='0.0.0.0', port=8000)
```

