from django.core.mail import send_mail
from django.core.mail import EmailMessage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Subscriber
from django.db import IntegrityError

@api_view(['POST'])
def subscribe(request):
    email = request.data.get('email', '')
    
    if not email:
        return Response({'error': 'Email is required'}, status=400)
    
    try:
        # Create subscriber
        subscriber = Subscriber.objects.create(email=email)
        
        # HTML Email content
        subject = "Welcome to Brew Your Experiences!"
        html_message = """
        <html>
        <body style="font-family: 'Helvetica Neue', Arial, sans-serif; color: #2c3e50; line-height: 1.6; padding: 20px;">
            <h1 style="color: #1a5f7a; font-size: 24px; margin-bottom: 20px;">Welcome to Brew Your Experiences!</h1>
            
            <p>Dear Explorer,</p>
            
            <p>Thank you for joining <strong>Brew Your Experiences</strong>! We're thrilled to have you as part of our travel community.</p>
            
            <h3 style="color: #1a5f7a; margin-top: 25px;">Here's what you can expect:</h3>
            
            <p>🌍 <strong>Curated Travel Insights:</strong> Exclusive guides and hidden gems from around the world</p>
            <p>✈️ <strong>Priority Access:</strong> Be the first to know about new experiences and destinations</p>
            <p>💎 <strong>Member Privileges:</strong> Special rates and early-bird offers on selected trips</p>
            
            <p style="margin-top: 25px;">Get ready for an incredible journey ahead. We're here to help craft unforgettable travel experiences just for you.</p>
            
            <p style="margin-top: 25px;">Follow us on <a href="https://www.instagram.com/brewyourexperiences/" style="color: #1a5f7a; text-decoration: none;">Instagram</a> for daily travel inspiration!</p>
            
            <hr style="border: none; border-top: 1px solid #eee; margin: 25px 0;">
            
            <p style="color: #666; font-size: 14px;">Brew Your Experiences Pvt. Ltd.<br>
            Charni Road, Mumbai</p>
            
            <p style="color: #666; font-size: 14px;">Questions? Simply reply to this email - we're here to help!</p>
        </body>
        </html>
        """
        
        # Send the email
        email_message = EmailMessage(
            subject=subject,
            body=html_message,
            from_email='brewyourexperiences@gmail.com',
            to=[email],
        )
        email_message.content_subtype = 'html'  # Set content type to HTML
        email_message.send()
        
        return Response({'message': 'Successfully subscribed'}, status=201)
    
    except IntegrityError:
        return Response({'error': 'This email is already subscribed.'}, status=400)
    except Exception as e:
        return Response({'error': str(e)}, status=400)
    
    
    
    
    
    
    # contact form email
    # views.py

@api_view(['POST'])
def contact_form(request):
    try:
        # Get form data
        name = request.data.get('name', '')
        email = request.data.get('email', '')
        phone = request.data.get('phone', '')
        message = request.data.get('message', '')
        
        if not all([name, email, message]):
            return Response({
                'error': 'Name, email and message are required'
            }, status=400)

        # Email to company
        company_subject = f"New Contact Form Submission from {name}"
        company_message = f"""
        <html>
        <body style="font-family: 'Helvetica Neue', Arial, sans-serif; color: #2c3e50; line-height: 1.6; padding: 20px;">
            <h2 style="color: #1a5f7a;">New Contact Form Submission</h2>
            
            <h3>Contact Details:</h3>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Phone:</strong> {phone}</p>
            
            <h3>Message:</h3>
            <p>{message}</p>
        </body>
        </html>
        """
        
        company_email = EmailMessage(
            subject=company_subject,
            body=company_message,
            from_email='brewyourexperiences@gmail.com',
            to=['brewyourexperiences@gmail.com'],
            reply_to=[email]
        )
        company_email.content_subtype = 'html'
        company_email.send()

        # Confirmation email to user
        user_subject = "Brew Your Experiences"
        user_message = f"""
        <html>
        <body style="font-family: 'Helvetica Neue', Arial, sans-serif; color: #2c3e50; line-height: 1.6; padding: 20px;">
            <h2 style="color: #1a5f7a;">Thank you for reaching out!</h2>
            
            <p>Dear {name},</p>
            
            <p>Thank you for contacting Brew Your Experiences! We have received your message and will get back to you shortly on WhatsApp or email.</p>
            
            <p>Follow us on Instagram for travel updates and inspiration:</p>
            <ul style="list-style: none; padding-left: 0;">
                <li><a href="https://www.instagram.com/brewyourexperiences/" style="color: #1a5f7a;">@brewyourexperiences</a></li>
                <li><a href="https://www.instagram.com/bbuzzz08/" style="color: #1a5f7a;">@bbuzzz08</a></li>
                <li><a href="https://www.instagram.com/theindianvacation/" style="color: #1a5f7a;">@theindianvacation</a></li>
            </ul>
            
            <hr style="border: none; border-top: 1px solid #eee; margin: 25px 0;">
            
            <p style="color: #666; font-size: 14px;">
                Regards,<br>
                Brew Your Experiences Pvt. Ltd.<br>
                Charni Road, Mumbai
            </p>
        </body>
        </html>
        """
        
        user_email = EmailMessage(
            subject=user_subject,
            body=user_message,
            from_email='brewyourexperiences@gmail.com',
            to=[email]
        )
        user_email.content_subtype = 'html'
        user_email.send()
        
        return Response({'message': 'Message sent successfully'}, status=200)
        
    except Exception as e:
        return Response({'error': str(e)}, status=400)
    
    
    # booking emails
    
@api_view(['POST'])
def handle_booking(request):
        try:
            # Get form data
            form_data = request.data
            
            # Find the selected trip details
            trips = [
                {
                    "id": 1,
                    "title": "Bali Sunset Adventure",
                    "highlight": "Most Popular",
                    "included": ["Return flights from major Indian cities", "4-star beach resort accommodation", 
                               "Daily breakfast and 4 special dinners", "Airport transfers and tour transportation",
                               "Guided tours to temples and cultural sites", "Hotel WiFi and local SIM card"],
                    "notIncluded": ["Travel insurance", "Optional activities", "Personal expenses", 
                                  "Visa fees", "Lunch and other meals not specified"]
                },
                {
                    "id": 2,
                    "title": "Japanese Culture Immersion",
                    "highlight": "Best Value",
                    "included": ["Return flights with premium carrier", "Mix of modern hotels and traditional ryokans",
                               "Daily breakfast and 6 authentic dinners", "Bullet train passes and local transport",
                               "Professional guides and entrance fees", "Portable WiFi device"],
                    "notIncluded": ["Travel insurance", "Optional activities", "Personal expenses",
                                  "Some local transport fares", "Meals not mentioned in itinerary"]
                },
                {
                    "id": 3,
                    "title": "Costa Rica Eco Tour",
                    "highlight": "Eco-friendly",
                    "included": ["Return flights with eco-conscious routing", "Eco-lodge accommodations",
                               "All meals with organic local produce", "Hybrid vehicle transfers",
                               "National park fees and guided tours", "Limited WiFi at lodges"],
                    "notIncluded": ["Travel insurance", "Optional adventures", "Personal expenses",
                                  "Carbon offset contribution (optional)", "Special equipment rental"]
                }
            ]
            
            selected_trip = next((trip for trip in trips if trip["id"] == form_data['selectedTrip']), None)
            
            # Send email to company
            company_subject = f"New Booking Request from {form_data['name']}"
            company_message = f"""
            <html>
            <body style="font-family: 'Helvetica Neue', Arial, sans-serif; color: #2c3e50; line-height: 1.6; padding: 20px;">
                <h2 style="color: #27C3C5;">New Booking Request</h2>
                
                <h3>Customer Details:</h3>
                <p><strong>Name:</strong> {form_data['name']}</p>
                <p><strong>Email:</strong> {form_data['email']}</p>
                <p><strong>Phone:</strong> {form_data['phone']}</p>
                <p><strong>Number of Travelers:</strong> {form_data['travelers']}</p>
                
                <h3>Selected Trip:</h3>
                <p><strong>Trip:</strong> {selected_trip['title']} ({selected_trip['highlight']})</p>
                
                <h4>Inclusions:</h4>
                <ul>
                    {' '.join(f'<li>{item}</li>' for item in selected_trip['included'])}
                </ul>
                
                <h4>Exclusions:</h4>
                <ul>
                    {' '.join(f'<li>{item}</li>' for item in selected_trip['notIncluded'])}
                </ul>
                
                <h3>Selected Extras:</h3>
                <p>{', '.join(str(extra) for extra in form_data['extras']) if form_data['extras'] else 'None'}</p>
                
                <h3>Additional Notes:</h3>
                <p>{form_data['notes'] or 'No additional notes'}</p>
            </body>
            </html>
            """
            
            company_email = EmailMessage(
                subject=company_subject,
                body=company_message,
                from_email='brewyourexperiences@gmail.com',
                to=['brewyourexperiences@gmail.com'],
                reply_to=[form_data['email']]
            )
            company_email.content_subtype = 'html'
            company_email.send()

            # Send confirmation email to customer
            customer_subject = "Your Booking Request - Brew Your Experiences"
            customer_message = f"""
            <html>
            <body style="font-family: 'Helvetica Neue', Arial, sans-serif; color: #2c3e50; line-height: 1.6; padding: 20px;">
                <h2 style="color: #27C3C5;">Thank You for Your Booking!</h2>
                
                <p>Dear {form_data['name']},</p>
                
                <p>We have received your booking request and our team will get in touch with you within 24 hours to discuss the details.</p>
                
                <h3 style="color: #27C3C5;">Booking Summary:</h3>
                <p><strong>Trip:</strong> {selected_trip['title']} ({selected_trip['highlight']})</p>
                <p><strong>Number of Travelers:</strong> {form_data['travelers']}</p>
                
                <h4 style="color: #27C3C5;">What's Included:</h4>
                <ul style="font-size: 0.9em;">
                    {' '.join(f'<li>{item}</li>' for item in selected_trip['included'])}
                </ul>
                
                <h4 style="color: #27C3C5;">What's Not Included:</h4>
                <ul style="font-size: 0.9em;">
                    {' '.join(f'<li>{item}</li>' for item in selected_trip['notIncluded'])}
                </ul>
                
                {f"<p><strong>Additional Notes:</strong> {form_data['notes']}</p>" if form_data['notes'] else ''}
                
                <p>Follow us on social media for travel updates and inspiration:</p>
                <ul style="list-style: none; padding-left: 0;">
                    <li><a href="https://www.instagram.com/brewyourexperiences/" style="color: #27C3C5;">@brewyourexperiences</a></li>
                </ul>
                
                <hr style="border: none; border-top: 1px solid #eee; margin: 25px 0;">
                
                <p style="color: #666; font-size: 14px;">
                    Regards,<br>
                    Brew Your Experiences Pvt. Ltd.<br>
                    Charni Road, Mumbai
                </p>
            </body>
            </html>
            """
            
            customer_email = EmailMessage(
                subject=customer_subject,
                body=customer_message,
                from_email='brewyourexperiences@gmail.com',
                to=[form_data['email']]
            )
            customer_email.content_subtype = 'html'
            customer_email.send()
            
            return Response({'message': 'Booking request received successfully'}, status=200)
            
        except Exception as e:
            return Response({'error': str(e)}, status=400)