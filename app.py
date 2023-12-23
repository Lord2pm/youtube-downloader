from flask import Flask, request, send_file, render_template, redirect, url_for, session, flash
from pytube import YouTube
import urllib
import os
from io import BytesIO


app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'


@app.get('/')
def index():
    return render_template("index.html")


@app.post('/pesquisar')
def pesquisar_video():
    try:
        link_video = request.form['link']
        session["link"] = link_video
        video = YouTube(link_video)
        return render_template("index.html", titulo=video.title, img=video.thumbnail_url)
    except urllib.error.URLError:
        flash("Verifique a sua conexão com a internet e tente novamente")
        return redirect(url_for("index"))


@app.post('/baixar')
def baixar():
    try:
        formato = request.form["formato"]
        link_video = session["link"]
        video = YouTube(link_video)
        buffer = BytesIO()

        if True:
            video = video.streams.filter(only_audio=True).first()
            video.stream_to_buffer(buffer)
            buffer.seek(0)
            out_file = video.download()
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            return send_file(buffer, download_name=new_file, as_attachment=True, mimetype="audio/mp3")
        else:
            video.streams.filter(only_audio=True, file_extension='mp3')
            video.stream_to_buffer(buffer)
            buffer.seek(0)
            video.streams.get_by_itag(18).download()

            return send_file(buffer, download_name=video, as_attachment=True, mimetype="video/mp4")
    except urllib.error.URLError:
        flash("Verifique a sua conexão com a internet e tente novamente")
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
