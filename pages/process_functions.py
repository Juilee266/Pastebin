from pages.models import Entry


def convert_text_to_link(text: str, base_url) -> str:
    ids = [e.id for e in Entry.objects.raw("SELECT id FROM pages_entry")]
    max_id = max(ids) if ids else 0
    id_ = max_id + 1
    db_id = f'{len(text)}_{id_}'
    save_to_db(id_, db_id, text)
    link = f"{base_url}/get_text?db_id={db_id}"
    return link


def save_to_db(index, db_id, text):
    e = Entry(index, db_id, text)
    e.save()


def delete_entry(db_id):
    Entry.objects.get(db_id=db_id).delete()
