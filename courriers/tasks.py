from celery import Celery
app = Celery()
app.conf.CELERY_ALWAYS_EAGER = True


@app.task
def subscribe(email, newsletter_list, lang=None, user=None):
    from courriers.backends import get_backend

    backend = get_backend()()

    try:
        backend.register(email=email,
                         newsletter_list=newsletter_list,
                         lang=lang,
                         user=user)
    except Exception as e:
        raise subscribe.retry(args=[email, newsletter_list, lang, user], exc=e, countdown=30)


@app.task
def unsubscribe(email, newsletter_list=None, lang=None, user=None):
    from courriers.backends import get_backend

    backend = get_backend()()

    try:
        backend.unregister(email=email,
                           newsletter_list=newsletter_list,
                           lang=lang,
                           user=user)
    except Exception as e:
        raise unsubscribe.retry(args=[email, newsletter_list, lang, user], exc=e, countdown=30)