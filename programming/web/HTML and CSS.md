# Html 
## discussing the structure of html file
```html
<!DOCTYPE html>   <!--  declarition of HTML Doc-->>

<html lang="en"> <!-- html tag: root of html file -->

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>my first website</title> <!-- what appears in the tab (name appears in the tab)-->

</head>

<body>

    <h1>this is a heading </h1>

</body>

</html>
```

### <u>lets break it up </u>

- `<!DOCTYPE html>` : declaration of html Document
- `<html> </html>` : represent the root element of html page 
- `<head> </head>` : describes the head of an html file , contain information about  the file 
- `<body> </body>` : the body of the html file , contains the content of the page 

# lets Discuss tags of HTML 
## Title
- title appears in the web browser tab
- title tag is written in the head partition
```html
<title> this is the title of the page</title>
```

## Heading
- heading tags used to heading in the page
- it starts with `<h1>` and ends with `<h6>`  
```html
      <h1> this is a heading</h1>

    <h2> this is the second heading</h2>

    <h3> this is the third heading</h3>

    <h4> this is the fourth heading</h4>

    <h5> this is the fifth heading</h5>

    <h6> this is the sixth heading</h6>
```

## Paragraphs
- adding paragraphs to the page
### two ways to add paragraphs
#### adding un-custom paragraph
- using the `<p> </p>` paragraph tag 
```html
<p> this is a mormal paragraph </p>
```
#### adding pre-custom paragraph 
- using `<pre> </pre>` paragraph tag
- **used when adding custom designed paragraph** 
```html
<pre>
this is a pre-customed paragraph
	You see that I have a unique style in writting 
		and that will appear in the page 
</pre>
```
## line break
- line break is used to add white spaces between elements
- using `<br>` tag (self closing tag) 
```html
<!-- adding a line break between elements-->
<br> 
```

## Horizontal  ruler
- its used to add a line (separating line) 
- using `<hr>` tag (self closing tag)
```html
<!-- adding a horizontal ruler-->
<hr>
```
