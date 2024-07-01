from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand
import random



class Command(BaseCommand):
   help = "This command inserts post data"

   def handle(self, *args: Any, **options: Any):

      # Delete existing data
      Post.objects.all().delete()

      titles = [
    "10 Tips for a Healthier Lifestyle",
    "Exploring the Hidden Gems of [Your City]",
    "The Ultimate Guide to Remote Work Success",
    "How to Cook the Perfect Steak at Home",
    "The Benefits of Meditation: A Beginner's Guide",
    "Top 5 Books to Read This Summer",
    "DIY Home Decor: Easy Projects to Transform Your Space",
    "The Rise of Electric Vehicles: What You Need to Know",
    "Mastering Time Management: Techniques for Busy Professionals",
    "Traveling on a Budget: Tips for Affordable Adventures",
    "The Importance of Mental Health Awareness",
    "How to Start Your Own Business from Scratch",
    "Sustainable Living: Eco-Friendly Practices for Everyday Life",
    "The Future of Artificial Intelligence: Trends and Predictions",
    "Fitness Myths Debunked: What Really Works",
    "Parenting Tips: Raising Happy and Healthy Kids",
    "The Art of Photography: Capturing Stunning Landscapes",
    "Investing 101: A Beginner's Guide to the Stock Market",
    "Delicious Vegan Recipes for Every Meal",
    "The Impact of Social Media on Modern Relationships"
]

      contents = [
    "Discover simple and effective tips to improve your lifestyle and boost your overall health.",
    "Join us as we explore the lesser-known attractions and hidden gems in [Your City].",
    "Learn the best practices and strategies for achieving success while working remotely.",
    "Follow our step-by-step guide to cooking a perfect steak right in your own kitchen.",
    "Understand the benefits of meditation and how to get started with this beginner's guide.",
    "Check out our top picks for must-read books that will keep you entertained this summer.",
    "Transform your home with these easy and budget-friendly DIY home decor projects.",
    "Stay informed about the rise of electric vehicles and what it means for the future.",
    "Learn time management techniques to boost your productivity and manage your busy schedule.",
    "Get tips and tricks for traveling on a budget without sacrificing the quality of your adventures.",
    "Explore the importance of mental health awareness and how to support those in need.",
    "Follow our guide on how to start your own business from scratch and achieve success.",
    "Incorporate eco-friendly practices into your daily life with our sustainable living tips.",
    "Stay ahead of the curve with trends and predictions about the future of artificial intelligence.",
    "Separate fact from fiction with our debunking of common fitness myths.",
    "Gain insights into raising happy and healthy kids with these essential parenting tips.",
    "Learn how to capture stunning landscapes with our comprehensive photography guide.",
    "Get started with investing and learn the basics of the stock market with this beginner's guide.",
    "Explore a variety of delicious vegan recipes that are perfect for every meal of the day.",
    "Understand the impact of social media on modern relationships and how to navigate it."
]

      img_urls = [
    "https://picsum.photos/id/1/800/400",
    "https://picsum.photos/id/2/800/400",
    "https://picsum.photos/id/3/800/400",
    "https://picsum.photos/id/4/800/400",
    "https://picsum.photos/id/5/800/400",
    "https://picsum.photos/id/6/800/400",
    "https://picsum.photos/id/7/800/400",
    "https://picsum.photos/id/8/800/400",
    "https://picsum.photos/id/9/800/400",
    "https://picsum.photos/id/10/800/400",
    "https://picsum.photos/id/11/800/400",
    "https://picsum.photos/id/12/800/400",
    "https://picsum.photos/id/13/800/400",
    "https://picsum.photos/id/14/800/400",
    "https://picsum.photos/id/15/800/400",
    "https://picsum.photos/id/16/800/400",
    "https://picsum.photos/id/17/800/400",
    "https://picsum.photos/id/18/800/400",
    "https://picsum.photos/id/19/800/400",
    "https://picsum.photos/id/20/800/400"
]

      categories = Category.objects.all()
      
      for title, content, img_url in zip(titles, contents, img_urls):
         category = random.choice(categories)
         Post.objects.create(title=title, content=content, img_url=img_url, category=category)

      self.stdout.write(self.style.SUCCESS("Completed inserting data!"))
      