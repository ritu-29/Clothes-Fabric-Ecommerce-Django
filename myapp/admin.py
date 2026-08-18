from django.contrib import admin
from .models import *
# Register your models here.
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from django.http import HttpResponse


def export_to_pdf(modeladmin, request, queryset):
    # Create a new PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # Generate the report using ReportLab
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Define styles
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        name='TitleStyle',
        parent=styles['Normal'],
        fontSize=20,
        fontName='Helvetica-Bold',
        spaceAfter=6,
        alignment=0  # Left align
    )

    subtitle_style = ParagraphStyle(
        name='SubtitleStyle',
        parent=styles['Normal'],
        fontSize=14,
        fontName='Helvetica',
        spaceAfter=12,
        alignment=0  # Left align
    )

    # Add title and subtitle
    # Add title and subtitle with spacing
    elements.append(Paragraph("Knit Fabric", title_style))
    elements.append(Spacer(1, 6))  # Space between title and subtitle
    elements.append(Paragraph("Order Report", subtitle_style))
    elements.append(Spacer(1, 12))  # Space after subtitle

    # Define the style for the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    # Create the table headers
    headers = ['user', 'amount', 'payment_mode', 'status', 'address', 'timestamp']

    # Create the table data
    data = []
    for obj in queryset:
        data.append([obj.user, obj.amount, obj.payment_mode, obj.status, obj.address, obj.timestamp])

    # Create the table
    t = Table([headers] + data, style=style)

    # Add the table to the elements array
    elements.append(t)

    # Build the PDF document
    doc.build(elements)

    return response


export_to_pdf.short_description = "Export to PDF"


@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'phone', "role", "status","id_proof")
    search_fields = ('name', 'email')

@admin.register(Contact_detail)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'timestamp')

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'date_of_birth', 'profession','bio','user_image')

@admin.register(SellerProfile)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'seller_image', 'shop_name', "shop_address", "years_of_experience","specialization","rating","availability")

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['cateName']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('seller','name','type' ,'measure','Cate','price', 'quantity', 'timestamp', 'image1','status')

@admin.register(productCart)
class ProductCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'Price', 'Quantity', 'total', 'Order_status', 'timeStamp')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'razorpay_order_id', 'razorpay_payment_id', 'razorpay_signature','payment_mode','status','offline_reference','offline_remarks','address')
    list_filter = ["timestamp"]
    actions = [export_to_pdf]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user','order','ratings','comment','timestamp')

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user','order','subject','description','timestamp')