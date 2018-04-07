import cairosvg

from django.core.mail import EmailMultiAlternatives
from django.utils.translation import ugettext_lazy as _


def get_ticket_subject(event_name):
    return _('Ticket for {event_name} event').format(event_name=event_name)


def get_ticket_body(first_name, last_name, event_name):
    body_txt = _(
        'Hello {first_name} {last_name},\n'
        'Here is your ticket for {event_name} event.\n'
        'Please remember to print it and bring it with you the day(s) of the event.\n'
        'Regards,\n'
        '{event_name} and eventoL team'
    ).format(
        first_name=first_name,
        last_name=last_name,
        event_name=event_name
    )
    body_html = _(
        '<p>Hello {first_name} {last_name},<br />\n'
        'Here is your ticket for {event_name} event.</p>\n'
        '<p>Please remember to <em>print it and bring it with you</em> the day(s) of the event.</p>\n'
        '<p>Regards,\n'
        '{event_name} and <em>eventoL</em> team</p>'
    ).format(
        first_name=first_name,
        last_name=last_name,
        event_name=event_name
    )
    return (body_txt, body_html)


def get_installation_subject(first_name, last_name, event_name):
    # ToDo: has FLISoL string
    return _(
        '{first_name} {last_name}, thank you for participating in FLISoL {event_name}'
    ).format(
        first_name=first_name, last_name=last_name, event_name=event_name
    )


def send_ticket_email(ticket_data, ticket_svg):
    event_name = ticket_data['event'].name
    first_name = ticket_data['first_name']
    last_name = ticket_data['last_name']
    email_to = ticket_data['email']
    ticket_code = ticket_data['ticket'].code
    email = EmailMultiAlternatives()
    email.subject = get_ticket_subject(event_name)
    body_txt, body_html = get_ticket_body(first_name, last_name, event_name)
    email.body = body_txt
    email.attach_alternative(body_html, "text/html")
    email.to = [email_to]
    email.attach('Ticket-{}.pdf'.format(ticket_code),
                 cairosvg.svg2pdf(bytestring=ticket_svg),
                 'application/pdf')
    email.send(fail_silently=False)


def send_installation_email(event_name, postinstall_email, attendee):
    email = EmailMultiAlternatives()
    first_name = attendee.first_name
    last_name = attendee.last_name
    email.subject = get_installation_subject(first_name, last_name, event_name)
    email.from_email = postinstall_email.contact_email
    email.body = ''
    email.attach_alternative(postinstall_email.message, "text/html")
    email.to = [attendee.email]
    email.send(fail_silently=False)