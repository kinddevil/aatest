package main

import(
"html/template"
"log"
"path"
"io"
"net/http"
"fmt"
"os"
"strings"
)

func hello(w http.ResponseWriter, r *http.Request){
  io.WriteString(w, "Hello")
}

func serveTemplate(w http.ResponseWriter, r *http.Request){
  lp:=path.Join("templates","layout.html")
  fp:=path.Join("templates",r.URL.Path)
  
  log.Println(r.URL.Path)

  info,err:=os.Stat(fp)
  if err!=nil{
    if os.IsNotExist(err){
      log.Println("path not found")
      http.NotFound(w,r)
      return
    }
  }

  if info.IsDir(){
    log.Println("Path is dir")
    http.NotFound(w,r)
  }

  tmpl, err:=template.ParseFiles(lp,fp)
  if err!=nil{
    log.Println(err.Error())
    http.Error(w, http.StatusText(500), 500)
    return
  }

  if err := tmpl.ExecuteTemplate(w, "layout", nil); err != nil {
    log.Println(err.Error())
    http.Error(w, http.StatusText(500), 500)
  }
}

func fview(w http.ResponseWriter, r *http.Request){
  log.Println(r.URL.Path)
  w.Header().Set("content-type", "text/html")
  pathInfo := strings.Trim(r.URL.Path, "/")
  //parts := strings.Split(pathInfo, "/")
  t, err := template.ParseFiles("templates/" + pathInfo + ".html")
  if err!=nil{
    log.Println(err.Error())
    http.NotFound(w, r)
    return
  }
  t.Execute(w, nil)  
  //io.WriteString(w, "view")
}

func main(){
  fs:=http.FileServer(http.Dir("Static"))
  http.Handle("/static/",http.StripPrefix("/static/",fs))
  http.HandleFunc("/",fview)
  //http.HandleFunc("/", serveTemplate)
  log.Println("listening...")
  fmt.Println("start server at 8000...")
  http.ListenAndServe(":8000",nil)
}
