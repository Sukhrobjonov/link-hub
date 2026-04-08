import os
from flask import Flask, render_template, redirect, request, abort
from google.cloud import firestore

app = Flask(__name__)

# Firestore bilan ulanish (App Engine o'z-o'zidan Gcp muhitiga ulanishni ta'minlaydi)
# Mahalliy (lokal) muhitda ishlash uchun GOOGLE_APPLICATION_CREDENTIALS muhit o'zgaruvchisi kerak bo'ladi
try:
    db = firestore.Client()
except Exception as e:
    print(f"Baza ulanmadi (lokal rejim uchun ruxsat yo'q): {e}")
    db = None

MOCK_LINKS = [
    {'id': '1', 'title': 'Loyihalarim', 'url': '/'}, 
    {'id': '2', 'title': 'Instagram', 'url': 'https://www.instagram.com/sukhrobjonov/'},
    {'id': '3', 'title': 'Telegram', 'url': 'https://t.me/Sukhrobjonov'}
]

@app.route('/')
def index():
    # Profil ma'lumotlari: uni hardcode qoldirish yoki uni ham bazadan o'qish mumkin.
    profile = {
        'name': 'Sukhrobjonov Javohir',
        'bio': 'Toza kod va zamonaviy dizayn asosida raqamli loyihalar yaratuvchi Dasturchi va Dizayner.',
        'avatar': '/static/yatoro.jpg?v=3'
    }

    links = []
    try:
        # Firestore'dan 'links' to'plamini 'order' bo'yicha tartiblab olish
        if db:
            links_ref = db.collection('links').order_by('order').stream()
            for doc in links_ref:
                link_data = doc.to_dict()
                link_data['id'] = doc.id
                links.append(link_data)
        else:
            links = MOCK_LINKS
    except Exception as e:
        # Firestore'dan o'qishda xatolik bo'lsa konsolga yozish
        print(f"Baza o'qishda xatolik: {e}")

    return render_template('index.html', profile=profile, links=links)


@app.route('/click/<link_id>')
def track_click(link_id):
    # Bosilgan havola hujjatini Firestore'dan olish
    if not db:
        # Lokal demo rejimda yo'naltirish
        for link in MOCK_LINKS:
            if link['id'] == link_id and link['url'] != '#':
                return redirect(link['url'])
        return redirect('/')

    doc_ref = db.collection('links').document(link_id)
    doc = doc_ref.get()

    if doc.exists:
        data = doc.to_dict()
        
        # 'clicks' hisoblagichini 1 ga oshirish
        doc_ref.update({
            'clicks': firestore.Increment(1)
        })
        
        # Havola yo'naltiriladigan asosiy manzil
        url = data.get('url')
        if url:
            return redirect(url)
        else:
            return abort(400, description="Ushbu havolaning URL manzili noto'g'ri sozlangan.")
    else:
         return abort(404, description="Bunday havola topilmadi.")

if __name__ == '__main__':
    # Local holatda serverni yurgizish
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
