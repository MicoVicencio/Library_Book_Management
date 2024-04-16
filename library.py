from datetime import datetime, timedelta
class Library:
    def __init__(self,
                 category=None,
                 name=None,
                 fiction_books=None,
                 non_fiction_books=None,
                 reference_books=None,
                 magazines = None,
                 academic_journals = None,
                 dvds = None,
                 cds_audio_books = None,
                 childrens_books = None,
                 educational_kits_games = None,
                 newspapers = None,
                 ):
        # Initialize all the attributes
        self.category = category
        self.name = name
        self.fiction_books = fiction_books
        self.non_fiction_books = non_fiction_books
        self.reference_books = reference_books
        self.magazines = magazines
        self.academic_journals = academic_journals
        self.dvds = dvds
        self.cds_audio_books = cds_audio_books
        self.childrens_books = childrens_books
        self.educational_kits_games = educational_kits_games
        self.newspapers = newspapers
        self.current_datetime = datetime.now()
        # Initialize lists of books and their copies
        # Each category has two copies of books initially
        self.fiction_books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "fiction_books"},
    {"title": "1984", "author": "George Orwell", "category": "fiction_books"}
]

        self.non_fiction_books = [
    {"title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "category": "non_fiction_books"},
    {"title": "The Power of Now", "author": "Eckhart Tolle", "category": "non_fiction_books"}
]

        self.reference_books = [
    {"title": "The Elements of Style", "author": "William Strunk Jr. & E.B. White", "category": "reference_books"},
    {"title": "Oxford Dictionary of English", "author": "Oxford Languages", "category": "reference_books"}
]

        self.magazines = [
    {"title": "National Geographic", "author": "Various", "category": "magazines"},
    {"title": "Time", "author": "Various", "category": "magazines"}
]

        self.newspapers = [
    {"title": "The New York Times", "author": "Various", "category": "newspapers"},
    {"title": "The Guardian", "author": "Various", "category": "newspapers"}
]

        self.academic_journals = [
    {"title": "Journal of Applied Psychology", "author": "Various", "category": "academic_journals"},
    {"title": "Journal of Molecular Biology", "author": "Various", "category": "academic_journals"}
]

        self.dvds = [
    {"title": "The Shawshank Redemption", "director": "Frank Darabont", "category": "dvds"},
    {"title": "Inception", "director": "Christopher Nolan", "category": "dvds"}
]

        self.cds_audio_books = [
    {"title": "Abbey Road", "artist": "The Beatles", "category": "cds_audio_books"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "cds_audio_books"}
]

        self.childrens_books = [
    {"title": "Charlotte's Web", "author": "E.B. White", "category": "childrens_books"},
    {"title": "Goodnight Moon", "author": "Margaret Wise Brown", "category": "childrens_books"}
]

        self.educational_kits_games = [
    {"title": "LEGO Mindstorms EV3", "type": "Robotics Kit", "category": "educational_kits_games"},
    {"title": "Scratch Coding Cards", "type": "Programming Game", "category": "educational_kits_games"}
]       
         # Initialize backup copies of books
        self.b_non_fiction_books = self.non_fiction_books.copy()
        self.b_fiction_books = self.fiction_books.copy()
        self.b_reference_books = self.reference_books.copy()
        self.b_magazines = self.magazines.copy()
        self.b_academic_journals = self.academic_journals.copy()
        self.b_dvds = self.dvds.copy()
        self.b_cds_audio_books = self.cds_audio_books.copy()
        self.b_childrens_books = self.childrens_books.copy()
        self.b_educational_kits_games = self.educational_kits_games.copy()
        self.b_newspapers = self.newspapers.copy()
        # Initialize lists for borrowed and reserved books, and borrowers/reservers
        self.bo_non_fiction_books = []
        self.bo_fiction_books = []
        self.bo_reference_books = []
        self.bo_magazines = self.magazines
        self.bo_academic_journals = []
        self.bo_dvds = []
        self.bo_cds_audio_books = []
        self.bo_childrens_books = [] 
        self.bo_educational_kits_games = []
        self.bo_newspapers = []
        self.borrowers = []
        self.reservers = []
        
        
        # Main library menu function
    def library_menu(self):
        print()
        print("Library Menu:")
        print("1.View Library Categories")
        print("2.Borrow Book in Library")
        print("3.Reserve Book in Library")
        print("4.View Borrowed/Reserved Books in Library")
        print("5.Exit Program")
        
        choice = input("Choose Library Functions:(1-5):")
        if choice == '1':
            self.view_category()
            self.library_menu()
        elif choice == '2':
            self.borrow()
        elif choice == '3':
            self.reservers_f()
        elif choice == '4':
            self.borrower_reserver_viewer()
        elif choice == '5':
            print("Exiting Program")
            exit()
        else:
            print("Invalid Input:Try Again!")
            self.library_menu()
            
     # Function to view different library categories               
    def view_category(self):
      print("Library Categories:")
      print("1. Fiction Books")
      print("2. Non-Fiction Books")
      print("3. Reference Books")
      print("4. Magazines")
      print("5. Newspapers")
      print("6. Academic Journals")
      print("7. DVDs")
      print("8. CDs/Audio Books")
      print("9. Children's Books")
      print("10. Educational Kits/Games")
      # Get user input for the desired category
      self.category = int(input("Enter the number of the category you want to view: "))
      # Print the selected category based on user input
      print()
      print("Available Books to be borrowed")
      if self.category == 1:
          print("\nFiction Books Catalog:")
          for book in self.b_fiction_books:
              print(f"Book Name: {book['title']}")
              print(f"Author: {book['author']}")
              print(f"Category: {book['category']}")
              print()
      elif self.category == 2:
          print("Non-Fiction Books Catalog:")
          for book in self.b_non_fiction_books:
            print(f"Book Name: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Category: {book['category']}")
            print()
      elif self.category == 3:
        print("Reference Books Catalog:")
        for book in self.b_reference_books:
            print(f"Book Name: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Category: {book['category']}")
            print()
      elif self.category == 4:
        print("Magazines Catalog:")
        for book in self.b_magazines:
            print(f"Book Name: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Category: {book['category']}")
            print()
      elif self.category == 5:
        print("Newspapers Catalog:")
        for book in self.b_newspapers:
            print(f"Book Name: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Category: {book['category']}")
            print()
      elif self.category == 6:
        print("Academic Journals Catalog:")
        for book in self.b_academic_journals:
            print(f"Book Name: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Category: {book['category']}")
            print()
      elif self.category == 7:
        print("DVDs Catalog:")
        for book in self.b_dvds:
            print(f"Book Name: {book['title']}")
            print(f"Director: {book['director']}")
            print(f"Category: {book['category']}")
            print()
      elif self.category == 8:
        print("CDs/Audio Books Catalog:")
        for book in self.b_cds_audio_books:
            print(f"Book Name: {book['title']}")
            print(f"Artist/Author: {book['artist'] if 'artist' in book else book['author']}")
            print(f"Category: {book['category']}")
            print()
      elif self.category == 9:
        print("Children's Books Catalog:")
        for book in self.b_childrens_books:
            print(f"Book Name: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Category: {book['category']}")
            print()
      elif self.category == 10:
        print("Educational Kits/Games Catalog:")
        for book in self.b_educational_kits_games:
            print(f"Book Name: {book['title']}")
            print(f"Type: {book['type']}")
            print(f"Category: {book['category']}")
            print()
      else:
        print("Invalid choice. Please enter a number between 1 and 10.")
      
      
    def borrow(self):# Function to borrow a book
        print("Borrowing Function")
        self.name = input("Enter your Name:")
        print("Choose Category:")
        self.view_category()
        choice = int(input("Choose Book(1-2):"))
        info = {}
        next_day = self.current_datetime + timedelta(days=1)
        if self.category == 1:
            if choice:# Move the selected book from available to borrowed
                self.bo_fiction_books.append(self.b_fiction_books[choice-1])
                self.b_fiction_books.pop(choice-1)
                info = {'Name': self.name,# Create borrowing info
                'Book Title':self.fiction_books[choice-1]['title'],
                'Author':self.fiction_books[choice-1]['author'],
                'Category':self.fiction_books[choice-1]['category'],
                'Date to be returned':next_day
                }
        elif self.category == 2:
            if choice:
                self.bo_non_fiction_books.append(self.b_non_fiction_books[choice-1])
                self.b_non_fiction_books.pop(choice-1)
                info = {'Name': self.name,
                'Book Title':self.non_fiction_books[choice-1]['title'],
                'Author':self.non_fiction_books[choice-1]['author'],
                'Category':self.non_fiction_books[choice-1]['category'],
                'Date to be returned':next_day
                }
        elif self.category == 3:
            if choice:
                self.bo_reference_books.append(self.b_reference_books[choice-1])
                self.b_reference_books.pop(choice-1)
                info = {'Name': self.name,
                'Book Title':self.reference_books[choice-1]['title'],
                'Author':self.reference_books[choice-1]['author'],
                'Category':self.reference_books[choice-1]['category'],
                'Date to be returned':next_day
                }
        elif self.category == 4:
            if choice:
                self.bo_magazines.append(self.b_magazines[choice-1])
                self.b_magazines.pop(choice-1)
                info = {'Name': self.name,
                'Book Title':self.magazines[choice-1]['title'],
                'Author':self.magazines[choice-1]['author'],
                'Category':self.magazines[choice-1]['category'],
                'Date to be returned':next_day
                }
        elif self.category == 5:
            if choice:
                self.bo_newspapers.append(self.b_newspapers[choice-1])
                self.b_newspapers.pop(choice-1)
                info = {'Name': self.name,
                'Book Title':self.newspapers[choice-1]['title'],
                'Author':self.newspapers[choice-1]['author'],
                'Category':self.newspapers[choice-1]['category'],
                'Date to be returned':next_day
                }
        elif self.category == 6:
            if choice:
                self.bo_academic_journals.append(self.b_academic_journals[choice-1])
                self.b_academic_journals.pop(choice-1)
                info = {'Name': self.name,
                'Book Title':self.academic_journals[choice-1]['title'],
                'Author':self.academic_journals[choice-1]['author'],
                'Category':self.academic_journals[choice-1]['category'],
                'Date to be returned':next_day
                }
        elif self.category == 7:
            if choice:
                self.bo_dvds.append(self.b_dvds[choice-1])
                self.b_dvds.pop(choice-1)
                info = {'Name': self.name,
                'Book Title':self.dvds[choice-1]['title'],
                'Author':self.dvds[choice-1]['director'],
                'Category':self.dvds[choice-1]['director'],
                'Date to be returned':next_day
                }
        elif self.category == 8:
            if choice:
                self.bo_cds_audio_books.append(self.b_cds_audio_books[choice-1])
                self.b_cds_audio_books.pop(choice-1)
                info = {'Name': self.name,
                'Book Title':self.cds_audio_books[choice-1]['title'],
                'Author':self.cds_audio_books[choice-1]['author'],
                'Category':self.cds_audio_books[choice-1]['category'],
                'Date to be returned':next_day
                }
        elif self.category == 9:
            if choice:
                self.bo_childrens_books.append(self.b_childrens_books[choice-1])
                self.b_childrens_books.pop(choice-1)
                info = {'Name': self.name,
                'Book Title':self.childrens_books[choice-1]['title'],
                'Author':self.childrens_books[choice-1]['author'],
                'Category':self.childrens_books[choice-1]['category'],
                'Date to be returned':next_day
                }
        elif self.category == 10:
            if choice:
                self.bo_educational_kits_games.append(self.b_educational_kits_games[choice-1])
                self.b_educational_kits_games.pop(choice-1)
                info = {'Name': self.name,
                'Book Title':self.educational_kits_games[choice-1]['title'],
                'Author':self.educational_kits_games[choice-1]['type'],
                'Category':self.educational_kits_games[choice-1]['category'],
                'Date to be returned':next_day
                } 
        print("Borrowing Book Complete!")
        self.borrowers.append(info)      
        self.library_menu()  
              
    def reserve(self):# Function to reserve a book
      print("Library Categories:")
      print("1. Fiction Books")
      print("2. Non-Fiction Books")
      print("3. Reference Books")
      print("4. Magazines")
      print("5. Newspapers")
      print("6. Academic Journals")
      print("7. DVDs")
      print("8. CDs/Audio Books")
      print("9. Children's Books")
      print("10. Educational Kits/Games")
      # Get user input for the desired category
      self.category = int(input("Enter the number of the category you want to view: "))
      # Print the selected category based on user input
      info = {}
      print()
      print("Available Books to be reserved")
      if self.category == 1:
          print("\nFiction Books Catalog:")
          for book in self.fiction_books:
              print(f"Book Name: {book['title']}")
              print(f"Author: {book['author']}")
              print(f"Category: {book['category']}")
              print()
      elif self.category == 2:
          print("Non-Fiction Books Catalog:")
          for book in self.non_fiction_books:
            print(f"Book Name: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Category: {book['category']}")
            print()
      elif self.category == 3:
        print("Reference Books Catalog:")
        for book in self.reference_books:
            print(f"Book Name: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Category: {book['category']}")
            print()
      elif self.category == 4:
        print("Magazines Catalog:")
        for book in self.magazines:
            print(f"Book Name: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Category: {book['category']}")
            print()
      elif self.category == 5:
        print("Newspapers Catalog:")
        for book in self.newspapers:
            print(f"Book Name: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Category: {book['category']}")
            print()
      elif self.category == 6:
        print("Academic Journals Catalog:")
        for book in self.academic_journals:
            print(f"Book Name: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Category: {book['category']}")
            print()
      elif self.category == 7:
        print("DVDs Catalog:")
        for book in self.dvds:
            print(f"Book Name: {book['title']}")
            print(f"Director: {book['director']}")
            print(f"Category: {book['category']}")
            print()
      elif self.category == 8:
        print("CDs/Audio Books Catalog:")
        for book in self.cds_audio_books:
            print(f"Book Name: {book['title']}")
            print(f"Artist/Author: {book['artist'] if 'artist' in book else book['author']}")
            print(f"Category: {book['category']}")
            print()
      elif self.category == 9:
        print("Children's Books Catalog:")
        for book in self.childrens_books:
            print(f"Book Name: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Category: {book['category']}")
            print()
      elif self.category == 10:
        print("Educational Kits/Games Catalog:")
        for book in self.educational_kits_games:
            print(f"Book Name: {book['title']}")
            print(f"Type: {book['type']}")
            print(f"Category: {book['category']}")
            print()
      else:
        print("Invalid choice. Please enter a number between 1 and 10.")
    
    def reservers_f(self):
        print("Reserving Function")
        self.name = input("Enter your Name:")
        print("Choose Category:")
        self.reserve()
        choice = int(input("Choose Book(1-2):"))
        info = {}
        if self.category == 1:
            if choice:
                info = {'Name': self.name,# Create reserving info
                'Book Title':self.fiction_books[choice-1]['title'],
                'Author':self.fiction_books[choice-1]['author'],
                'Category':self.fiction_books[choice-1]['category']
                }
        elif self.category == 2:
            if choice:
                info = {'Name': self.name,
                'Book Title':self.non_fiction_books[choice-1]['title'],
                'Author':self.non_fiction_books[choice-1]['author'],
                'Category':self.non_fiction_books[choice-1]['category']
                }
        elif self.category == 3:
            if choice:
                info = {'Name': self.name,
                'Book Title':self.reference_books[choice-1]['title'],
                'Author':self.reference_books[choice-1]['author'],
                'Category':self.reference_books[choice-1]['category']
                }
        elif self.category == 4:
            if choice:
                info = {'Name': self.name,
                'Book Title':self.magazines[choice-1]['title'],
                'Author':self.magazines[choice-1]['author'],
                'Category':self.magazines[choice-1]['category']
                }
        elif self.category == 5:
            if choice:
                info = {'Name': self.name,
                'Book Title':self.newspapers[choice-1]['title'],
                'Author':self.newspapers[choice-1]['author'],
                'Category':self.newspapers[choice-1]['category']
                }
        elif self.category == 6:
            if choice:
                info = {'Name': self.name,
                'Book Title':self.academic_journals[choice-1]['title'],
                'Author':self.academic_journals[choice-1]['author'],
                'Category':self.academic_journals[choice-1]['category']
                }
        elif self.category == 7:
            if choice:
                info = {'Name': self.name,
                'Book Title':self.dvds[choice-1]['title'],
                'Author':self.dvds[choice-1]['director'],
                'Category':self.dvds[choice-1]['category']
                }
        elif self.category == 8:
            if choice:
                info = {'Name': self.name,
                'Book Title':self.cds_audio_books[choice-1]['title'],
                'Author':self.cds_audio_books[choice-1]['author'],
                'Category':self.cds_audio_books[choice-1]['category']
                }
        elif self.category == 9:
            if choice:
                info = {'Name': self.name,
                'Book Title':self.childrens_books[choice-1]['title'],
                'Author':self.childrens_books[choice-1]['author'],
                'Category':self.childrens_books[choice-1]['category']
                }
        elif self.category == 10:
            if choice:
                info = {'Name': self.name,
                'Book Title':self.educational_kits_games[choice-1]['title'],
                'Author':self.educational_kits_games[choice-1]['type'],
                'Category':self.educational_kits_games[choice-1]['category']
                } 
        print("Reserving Book Complete!")
        self.reservers.append(info)      
        self.library_menu()
        
    # Function to view borrowed/reserved books    
    def borrower_reserver_viewer(self):
        print("What do you want to see?")
        print("1.Borrowed Books")
        print("2.Reserved Books")
        print("3.Back to Main Menu")
        choice = input("Enter your Choice:(1-3):")
        print()
        if choice == '1':
          print("List of Borrowers:")
          for info in self.borrowers:
            print(f"Name: {info['Name']}")
            print(f"Book Title: {info['Book Title']}")
            print(f"Author: {info['Author']}")
            print(f"Category: {info['Category']}")
            print(f"Date to be returned:{info['Date to be returned']}")
            print()
        elif choice == '2':
            print("List of Reserved Books:")
            for info in self.reservers:
              print(f"Name: {info['Name']}")
              print(f"Book Title: {info['Book Title']}")
              print(f"Author: {info['Author']}")
              print(f"Category: {info['Category']}")
        elif choice == '3':
            self.library_menu()
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
            self.borrower_reserver_viewer()
        self.library_menu()  
        
                 
main= Library()
main.library_menu()
