from flask import Flask, render_template, request, redirect,  url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/music_event')
def event():
    return render_template('music_event.html')

@app.route('/detail_event')
def detail_event():
    event_id = request.args.get('event_id')

    sample_events = {
        "1": {
            "name": "Đêm nhạc Acoustic",
            "date": "2025-08-15",
            "formatted_date": "15/08/2025",
            "location": "Hà Nội",
            "price": "100,000 VND",
            "image": "images/1.jpg"
        },
        "2": {
            "name": "Hội chợ Sách",
            "date": "2025-09-01",
            "formatted_date": "01/09/2025",
            "location": "TP.HCM",
            "price": "Miễn phí",
            "image": "images/2.jpg"
        }
    }

    event = sample_events.get(event_id)

    if not event:
        return "Sự kiện không tồn tại", 404

    return render_template('detail_event.html', event=event, event_id=event_id)


@app.route('/book_ticket')
def book_ticket():
    event_id = request.args.get('event_id')

    sample_events = {
        "1": {
            "id": 1,
            "ten": "Đêm nhạc Acoustic  ",
            "ngay": "15/08/2025",
            "thoigian": "19:00",
            "diadiem": "Hà Nội"
        },
        "2": {
            "id": 2,
            "ten": "Hội chợ Sách",
            "ngay": "01/09/2025",
            "thoigian": "08:00",
            "diadiem": "TP.HCM"
        }
    }

    show = sample_events.get(event_id)

    if not show:
        return "Sự kiện không tồn tại", 404

    ticket = {
        "loaive": "VIP",
        "soluong": 1,
        "gia": 500000,
        "tong": 500000
    }

    return render_template('book_ticket.html', show=show, ticket=ticket)



@app.route("/organizer")
def organizer_header():
    return render_template("organizer.html")

@app.route("/create_event")
def create_event():
    return render_template("create_event.html")

@app.route("/my_event")
def my_event():
    return render_template("my_event.html")

@app.route("/report_event")
def report_event():
    return render_template("report_event.html")

if __name__ == '__main__':
    app.run(debug=True)