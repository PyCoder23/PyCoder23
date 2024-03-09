// It might be possible that you encounter error(s) while running this because of library(s) not installed or accessible.
// But this will surely help you in your programs. All the BEST!

import java.sql.*;
import java.util.*;
import java.util.Date;
import java.util.concurrent.TimeUnit;

import mypack.LocalMySQL;
import java.text.SimpleDateFormat;

class Library {
    public static ArrayList <Book> BookObs = new ArrayList <Book>();
    public static ArrayList <String> Borrows = new ArrayList <String>();
    static ResultSet resultSet3, resultSet5, resultSet6;

    Books MyO = new Books();
    
    public void addBook(Book book){
        BookObs.add(book);
    }

    public boolean checkIf(){
        boolean isLen = true;
        if (BookObs.size() == 0){
            isLen = false;
        }
        return isLen;
    }

    public String removeBook(String isbn){
        Books I = new Books(); 
        String don = "1";

        isbn = BookObs.get(0).mdIsb(isbn);
        System.out.println(Books.listIsb);
        if (Books.listIsb.contains(isbn)){
            if (!(Borrows.contains(isbn))){
                int ind = Books.listIsb.indexOf(isbn);

                String bookn = BookObs.get(ind).getTitle();

                System.out.println("\nPlease confirm!");
                System.out.print("Are you sure that book "+bookn+" is to be deleted (Y/N) ? ");
                String Io = I.getIn();

                Io = Io.toUpperCase();

                while (!(Io.equals("Y")) && !(Io.equals("N"))){
                    System.out.println("Invalid Input!");
                    System.out.print("Are you sure that book "+bookn+" should be deleted (Y/N) ? ");
                    Io = I.getIn();
                    Io = Io.toUpperCase();
                }

                if (Io.equals("Y")){
                    BookObs.remove(ind);
                    Books.listIsb.remove(ind);
                    return bookn;
                }
                else {
                    don = "2";
                }
            }
            else{
                don = "3";
            }
        } else {
            don = "0";
        }

        return don;
    }

    public void dispayBooks(){
        try {
            resultSet5 = (Books.statement).executeQuery("select count(*) from books");

            resultSet5.next();
            if (resultSet5.getInt(1) == 0){
                System.out.println("\nNo Book In the Library!");
                resultSet5.close();
            } 
            else {
                resultSet3 = (Books.statement).executeQuery("select * from books");
                System.out.println("\nDisplaying All Books!\n");
                int i = 1;
                while (resultSet3.next()) {
                    String title = resultSet3.getString("title");
                    String auth = resultSet3.getString("author").trim();
                    String isbn = resultSet3.getString("isbn");
                    int nuP = resultSet3.getInt("pages");
                    int gen = resultSet3.getInt("genre");
                    boolean av = resultSet3.getBoolean("avail");

                    PreparedStatement mys7 = (Books.connection).prepareStatement("select * from genres where ID = ?");
                    mys7.setInt(1, gen);
                    resultSet6 = mys7.executeQuery();
                    resultSet6.next();
                    String genre = resultSet6.getString("genre");

                    System.out.println("Book Serial Number -> "+i);
                    System.out.println("Book's Title -> "+title);
                    System.out.println("Book's Author -> "+auth);
                    System.out.println("Book's Isbn -> "+isbn);
                    System.out.println("Book's Genre -> "+genre);
                    System.out.println("Book's Number of pages -> "+nuP);
                    System.out.println("Book Available ? -> "+av);
                    System.out.println();
                    i += 1;
                }
                resultSet3.close();
            } 
        }
        catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public String borrowBook(String isbn){
        Books I = new Books(); 
        String done = "1";
        
        isbn = BookObs.get(0).mdIsb(isbn);

        if (Books.listIsb.contains(isbn)){
            if (!(Borrows.contains(isbn))){
                int ind = Books.listIsb.indexOf(isbn);

                String bookn = BookObs.get(ind).getTitle();

                System.out.println("\nPlease confirm!");
                System.out.print("Are you sure that book "+bookn+" is to be borrowed (Y/N) ? ");
                String Io = I.getIn();

                Io = Io.toUpperCase();

                while (!(Io.equals("Y")) && !(Io.equals("N"))){
                    System.out.println("Invalid Input!");
                    System.out.print("Are you sure that book "+bookn+" should be borrowed (Y/N) ? ");
                    Io = I.getIn();
                    Io = Io.toUpperCase();
                }

                if (Io.equals("Y")){
                    Borrows.add(isbn);
                    return bookn;
                }
                else {
                    done = "2";
                }
            }
            else{
                done = "3";
                System.out.println(Borrows);
            }
        } else {
            done = "0";
        }

        return done;
    }

    public String returnBook(String isbn){
        Books I = new Books(); 
        String done = "1";
        
        isbn = BookObs.get(0).mdIsb(isbn);

        if (Books.listIsb.contains(isbn)){
            if (Borrows.contains(isbn)){
                int ind = Books.listIsb.indexOf(isbn);

                String bookn = BookObs.get(ind).getTitle();

                System.out.println("\nPlease confirm!");
                System.out.print("Are you sure that book "+bookn+" is to be returned (Y/N) ? ");
                String Io = I.getIn();

                Io = Io.toUpperCase();

                while (!(Io.equals("Y")) && !(Io.equals("N"))){
                    System.out.println("Invalid Input!");
                    System.out.print("Are you sure that book "+bookn+" should be returned (Y/N) ? ");
                    Io = I.getIn();
                    Io = Io.toUpperCase();
                }

                if (Io.equals("Y")){
                    Borrows.remove(isbn);
                    return bookn;
                }
                else {
                    done = "2";
                }
            }
            else{
                done = "3";
            }
        } else {
            done = "0";
        }

        return done;
    }

    public void displayLib(){
        System.out.print("The list containing Borrowed Books is :");
        System.out.println(Borrows);
        System.out.println();
    }
    
}

class Book{

    Books MyOBb = new Books();

    String title = "";
    String author = "";
    String isbn = "";
    String genre = "";
    String Uisbn = "";
    String language = "";
    int numPages = 0;
    boolean available = false;    

    //Setters
    public void setTitle(String T){
        this.title = T;
    }

    public void setAuthor(String A){
        this.author = A;
    }

    public void setGenre(String genre){
        this.genre = genre;
    }

    public String mdIsb(String isb){
        String Md = "";

        for (int i = 0; i < isb.length(); i++){

            if (Character.isDigit(isb.charAt(i))){
                Md = Md + (String.valueOf(isb.charAt(i)));
            }
        }
        
        return Md;
    }

    public String udIsb(String isb){
        String Ud = "";

        for (int i = 0; i < isb.length(); i++){
            if ((Character.isDigit(isb.charAt(i))) || ((isb.charAt(i)) == '-')){
                Ud = Ud + (String.valueOf(isb.charAt(i)));
            }
        }
        
        return Ud;
    }

    public void setIsbn(String Isb, String Usb){
        Books.listIsb.add(Isb);
        this.isbn = Isb;
        this.Uisbn = Usb;
    }

    public String checkIsbn(String isb){
        String MyIsb = "";
        String UsIsb;

        String go = "1";

        MyIsb = mdIsb(isb);
        UsIsb = udIsb(isb);

        //System.out.println("Good -> "+UsIsb);

        if ((MyIsb.length() != 10) && (MyIsb.length() != 13)){
            System.out.println("\nInvalid isbn!");
            System.out.println("ISBN must contain either 10 or 13 digits!\n");
            go = "0";
        }
        else {

            if (MyIsb.length() == 10){
                int sum = 0;
                for (int i = 0; i < 10 ; i++){
                    int dig = Integer.parseInt(String.valueOf(MyIsb.charAt(i)));
                    int a = 10 - i;
                    sum += (a*dig);
                }
                //System.out.println("Sum -> "+sum);

                if (sum % 11 != 0){
                    System.out.println("\nInvalid isbn!");
                    System.out.println("ISBN does not exist!\n");
                    go = "0";
                }
            }

            else {
                int sum = 0;
                for (int i = 0; i < 13 ; i++){
                    int dig = Integer.parseInt(String.valueOf(MyIsb.charAt(i)));
                    
                    int a;
                    if (i % 2 == 0){
                        a = 1;
                    } else {
                        a = 3;
                    }

                    sum += (a*dig);
                }
                //System.out.println("Sum -> "+sum);

                if (sum % 10 != 0){
                    System.out.println("\nInvalid isbn!");
                    System.out.println("ISBN does not exist!\n");
                    go = "0";
                } 
            }

            if (Books.listIsb.contains(MyIsb)){
                System.out.println("\nExisting Book!");
                System.out.println("Book with this ISBN already exists!\n");
                go = "2";
            } 
            else {
                setIsbn(MyIsb, UsIsb);
            }
        }

        return go;
    }

    public void setNumPages(int numP){
        this.numPages = numP;
    }

    public void setAvail(boolean Ava){
        this.available = Ava;
    }

    //Getters
    public String getTitle(){
        return title;
    }
    
    public String getAuth(){
        return author;
    }

    public String getIsbn(){
        return Uisbn;
    }

    public String getGenre(){
        return genre;
    }

    public String getMsbn(){
        return isbn;
    }

    public int getNumPages(){
        return numPages;
    }

    public boolean getAvail(){
        return available;
    }

}

public class Books{
    public static ArrayList <String> listIsb = new ArrayList <String>();
    static Book my; 
    static Scanner me = new Scanner(System.in);
    public static String nam;
    static Statement statement;
    public static String email;
    static Connection connection;

    public String getIn(){
        String myI = me.nextLine();
        return myI;
    }

    public static void main(String[] args) {
        LocalMySQL.main(args);
        String pas = "PASSWORD";
        Library myObj = new Library();

        try {
            LocalMySQL.Connect("lib", pas);
            connection = LocalMySQL.relC();
            statement = LocalMySQL.relS();

            ResultSet resultSetA;
            resultSetA = statement.executeQuery("select title, author, isbn, pages, avail from books");

            while(resultSetA.next()){
                Book xy = new Book();
                myObj.addBook(xy);
                
                xy.setTitle(resultSetA.getString(1));
                xy.setAuthor(resultSetA.getString(2));
                xy.setIsbn(resultSetA.getString(3), resultSetA.getString(3));
                xy.setNumPages(resultSetA.getInt(4));
                xy.setAvail(resultSetA.getBoolean(5));

                if (!(resultSetA.getBoolean(5))){
                    Library.Borrows.add(resultSetA.getString(3));
                }
            }

            System.out.println("Welcome to Library System"); 
            System.out.println("We Hope our Service Fulfils your Task!\n"); 

            System.out.print("Are you an existing user (y/n) ?");
            String ch1 = me.nextLine();
            ch1 = ch1.toUpperCase();

            while (!(ch1.equals("Y")) && !(ch1.equals("N"))){
                System.out.println("\nInvalid Input!");
                System.out.print("Are you an existing user (y/n) ?");
                ch1 = me.nextLine();
                ch1 = ch1.toUpperCase();
            }

            boolean log = true;

            while (log){
                if (ch1.equals("Y")){
                    System.out.println("Please Login to Use our Services: \n");
                    boolean isReg = false;

                    while(!(isReg)){

                        System.out.print("Please Enter your Email : ");
                        email = (me.nextLine()).toLowerCase();

                        System.out.print("Please Enter your Password : ");
                        String pass = (me.nextLine()).toLowerCase();

                        ResultSet resultSet1;
                        resultSet1 = statement.executeQuery("select Name, Email, Password from credentials");
                        
                        isReg = false;
                        while(resultSet1.next()){
                            if (((resultSet1.getString(2)).toLowerCase()).equals(email)){
                                if (((resultSet1.getString(3)).toLowerCase()).equals(pass)){
                                    isReg = true;
                                    nam = resultSet1.getString(1);
                                }
                            }                        
                        }

                        if (isReg){
                            ResultSet resB;
                            PreparedStatement msA = connection.prepareStatement("select Inactive from Credentials where email = ?");         
                            msA.setString(1, email);
                            resB = msA.executeQuery();
                            resB.next();
                            int ina = resB.getInt(1);
                            
                            if (ina == 0){
                                System.out.println("\nLogin Successfully!");
                                System.out.println("Welcome "+nam+"!");
                                log = false;
                            }
                            else {
                                System.out.println("\nYour account is Inactive!");
                                System.out.println("Login unsuccessful!");
                                isReg = false;
                            }
                        }
                        else {
                            System.out.println("\nLogin Credentials Invalid!");
                            System.out.println("Please try again!\n");
                        }
                        
                        resultSet1.close();
                    }
                }

                else {
                    System.out.println("Please register to start using our services: \n");
                    boolean isAva = false;

                    System.out.print("Please Enter your Name : ");
                    String name = me.nextLine();

                    while(!(isAva)){

                        System.out.print("Please Enter your Email : ");
                        email = (me.nextLine()).toLowerCase();

                        ResultSet resultSet2;
                        resultSet2 = statement.executeQuery("select Name, Email, Password from credentials");
                        
                        isAva = true;
                        while(resultSet2.next()){
                            if (((resultSet2.getString(2)).toLowerCase()).equals(email)){
                                isAva = false;
                            }
                        }

                        if (isAva){
                            isAva = true; 
                            System.out.print("Please Enter your Password : ");
                            String pass = (me.nextLine()).toLowerCase();

                            System.out.print("Please Enter your Date Of Birth (mm/dd/yyyy) : ");
                            String dob = (me.nextLine()).toLowerCase();

                            System.out.print("Please Enter your gender (male/female) : ");
                            String gen = (me.nextLine()).toLowerCase();
                            gen = gen.toLowerCase();

                            while (!(gen.equals("male")) && !(gen.equals("female"))){
                                System.out.println("\nInvalid Input!");
                                System.out.print("Please Enter your gender (male/female) : ");
                                gen = (me.nextLine()).toLowerCase();
                                gen = gen.toLowerCase();
                            }

                            PreparedStatement mys = connection.prepareStatement("INSERT into Credentials (Name, Email, Password, DOB, Gender, Score, Inactive) VALUE (?, ?, ?, ?, ?, ?, ?)");
                            mys.setString(1, name);
                            mys.setString(2, email);
                            mys.setString(3, pass);
                            mys.setString(4, dob);
                            mys.setString(5, gen);
                            mys.setInt(6, 500);
                            mys.setInt(7, 0);
                            mys.executeUpdate();

                            System.out.println("\nRegistration Successful!");
                            System.out.println("Your initial Credit Score is 500 on a scale of 300 to 900!");
                            ch1 = "Y";
                        }
                        else {
                            System.out.println("\nEmail already registered with Us!");
                            ch1 = "Y";
                            isAva = true;
                        }
                        
                        resultSet2.close();
                    }
                }
            }

            String use = "Y";
            Boolean Ina = true;
            while (use.equals("Y") && Ina){
                System.out.println("\nPlease enter 1 to Add a new Book!"); 
                System.out.println("Please enter 2 to Remove a Book!"); 
                System.out.println("Please enter 3 to Borrow a Book!"); 
                System.out.println("Please enter 4 to Return a Book!"); 
                System.out.println("Please enter 5 to Display all Books!"); 

                System.out.print("\nPlease enter a command: "); 
                String Choice = me.nextLine();

                boolean isInt = true;

                for (int i = 0; i< Choice.length(); i++){
                    if (!(Character.isDigit(Choice.charAt(i)))){
                        isInt = false;
                    }
                    if (!((Choice.charAt(i)) == '1') && !((Choice.charAt(i)) == '2') && !((Choice.charAt(i)) == '3') && !((Choice.charAt(i)) == '4') && !((Choice.charAt(i)) == '5')){
                        isInt = false;
                    }
                }

                while (!(isInt)){
                    System.out.print("\nInvalid Input!");
                    System.out.print("Please enter from existing commands only!");  
                    System.out.print("\nPlease enter a command: "); 
                    Choice = me.nextLine();
                    isInt = true;
                    if (Choice.equals("")){
                        isInt = false;
                    }
                    for (int i = 0; i< Choice.length(); i++){
                        if (!(Character.isDigit(Choice.charAt(i)))){
                            isInt = false;
                        } 
                        if (!((Choice.charAt(i)) == '1') && !((Choice.charAt(i)) == '2') && !((Choice.charAt(i)) == '3') && !((Choice.charAt(i)) == '4') && !((Choice.charAt(i)) == '5')){
                            isInt = false;
                        }
                    }
                }

                int com = Integer.parseInt(Choice);

                my = new Book();
            
                if (com == 1){

                    System.out.println("\nTo add a new Book :\n");

                    System.out.print("Please enter book name :");
                    String tit = me.nextLine(); 

                    if (tit.equals("") || tit.equals(" ")){
                        isInt = false;
                    }
                    
                    int n = 0;
                    while (!(isInt)){
                        n = 1;
                        System.out.println("\nInvalid Input!");
                        System.out.println("Blank book name!");  
                        System.out.print("Please enter book's name :");
                        tit = me.nextLine(); 
                        isInt = true;
                        if (tit.equals("")){
                            isInt = false;
                        }
                    }

                    if (n == 1){
                        System.out.println();
                    }
                    
                    System.out.print("Please enter book's author name :");
                    String auth = me.nextLine(); 

                    if (auth.equals("") || auth.equals(" ")){
                        isInt = false;
                    }
                    
                    int m = 0;
                    while (!(isInt)){
                        m = 1;
                        System.out.println("\nInvalid Input!");
                        System.out.println("Blank author name!");  
                        System.out.print("Please enter book's author name :");
                        auth = me.nextLine(); 
                        isInt = true;
                        if (auth.equals("")){
                            isInt = false;
                        }
                    }

                    if (m == 1){
                        System.out.println();
                    }

                    System.out.print("Please enter book's isbn :");
                    String isbn = me.nextLine(); 

                    boolean Exis = false;

                    ResultSet resultSet4;
                    resultSet4 = statement.executeQuery("select isbn from books");
                    
                    Book xz = new Book(); 
                    while(resultSet4.next()){
                        if (((resultSet4.getString(1)).toLowerCase()).equals(xz.mdIsb(isbn))){
                            Exis = true;
                        }
                    }
                    
                    String go;
                    if(!(Exis)){
                        go = my.checkIsbn(isbn);
                    }
                    else {
                        go = "2";
                        System.out.println("\nExisting Book");
                        System.out.println("Book with this isbn already exists!\n");
                    }

                    while (go.equals("0")){
                        System.out.print("Please enter book's isbn :");
                        isbn = me.nextLine(); 
                        go = my.checkIsbn(isbn);
                    } 

                    if (go.equals("1")){
                        myObj.addBook(my);
                        my.setTitle(tit);
                        my.setAuthor(auth);

                        System.out.print("Please enter book's genre :");
                        String genre = me.nextLine(); 

                        boolean isGen = false;
                        ResultSet resultSet9 = statement.executeQuery("select * from genres");
                        while(resultSet9.next()){
                            if ((resultSet9.getString("genre").toLowerCase().trim()).equals(genre.toLowerCase().trim())){
                                isGen = true;
                            }
                        }

                        while (!(isGen)) {
                            System.out.println("\nInvalid Input!");
                            System.out.println("Genre does not exist!\n");
                            System.out.print("Please enter book's genre :");
                            genre = me.nextLine(); 

                            isGen = false;
                            resultSet9 = statement.executeQuery("select * from genres");
                            while(resultSet9.next()){
                                if ((resultSet9.getString("genre").toLowerCase().trim()).equals(genre.toLowerCase().trim())){
                                    isGen = true;
                                }
                            }
                        }

                        my.setGenre(genre);

                        System.out.print("Please enter book's number of pages :");
                        String numPage = me.nextLine(); 

                        for (int i = 0; i< numPage.length(); i++){
                            if (!(Character.isDigit(numPage.charAt(i)))){
                                isInt = false;
                            }
                        }
            
                        while (!(isInt)){
                            System.out.print("\nInvalid Input!");
                            System.out.print("Please enter integar value only!");  
                            System.out.print("\nPlease enter book's number of pages: "); 
                            numPage = me.nextLine();
                            isInt = true;
                            if (numPage.equals("")){
                                isInt = false;
                            }
                            for (int i = 0; i< numPage.length(); i++){
                                if (!(Character.isDigit(numPage.charAt(i)))){
                                    isInt = false;
                                } 
                            }
                        }

                        my.setNumPages(Integer.parseInt(numPage));
                        my.setAvail(true);

                        System.out.println("\nBook's Title -> "+my.getTitle());
                        System.out.println("Book's Author -> "+my.getAuth());
                        System.out.println("Book's Isbn -> "+my.getIsbn());
                        System.out.println("Book's Genre -> "+my.getGenre());
                        System.out.println("Book's Number of pages -> "+my.getNumPages());
                        System.out.println("Book Available ? -> "+my.getAvail());
                        System.out.println();

                        PreparedStatement mys7 = connection.prepareStatement("select * from genres where genre = ?");
                        mys7.setString(1, my.getGenre());
                        ResultSet resultSet6 = mys7.executeQuery();
                        resultSet6.next();
                        int gen = resultSet6.getInt("id");

                        PreparedStatement mys = connection.prepareStatement("INSERT into Books (Title, Author, isbn, Genre, Pages, Avail) VALUE (?, ?, ?, ?, ?, ?)");
                        mys.setString(1, my.getTitle());
                        mys.setString(2, my.getAuth());
                        mys.setString(3, my.getMsbn());
                        mys.setInt(4, gen);
                        mys.setInt(5, my.getNumPages());
                        mys.setBoolean(6, my.getAvail());
                        mys.executeUpdate();
                    }
                }

                if (com == 2){

                    boolean IsLen = myObj.checkIf();
                    if (IsLen){
                        System.out.println("\nTo remove a Book :");
                        System.out.print("Please enter isbn of the book : ");
                        String isb = me.nextLine();
                        String don = myObj.removeBook(isb);

                        while (don.equals("0")){
                            System.out.println("\nBook with ISBN does not exist!\n");

                            System.out.print("Please enter isbn of the book : ");
                            isb = me.nextLine();
                            don = myObj.removeBook(isb);
                        }

                        if (don.equals("2")){
                            System.out.println("\nOk!");
                            System.out.println("Book not Deleted!");
                        } else if (don.equals("3")){
                            System.out.println("\nBook Borrowed by another user!");
                            System.out.println("Book not Deleted!");                        
                        }else {
                            System.out.println("\nDone!");
                            System.err.println("Book "+don+" successfully deleted!");

                            Book a = new Book();
                            isb = a.mdIsb(isb);

                            PreparedStatement ms = connection.prepareStatement("delete from books where isbn = ?");
                            ms.setString(1, isb);
                            ms.executeUpdate();
                        }
                        System.out.println();
                    } else {
                        System.out.println("\nNo Book present in the library!\n");
                    }
                }

                if (com == 3){
                    boolean IsLen = myObj.checkIf();
                    if (IsLen){
                        Library myOb = new Library();
                        myOb.dispayBooks();

                        System.out.println("To borrow a Book :");
                        System.out.print("Please enter isbn of the desired book : ");
                        String isb = me.nextLine();
                        String don = myObj.borrowBook(isb);

                        while (don.equals("0")){
                            System.out.println("\nBook with ISBN does not exist!\n");

                            System.out.print("Please enter isbn of the book : ");
                            isb = me.nextLine();
                            don = myObj.borrowBook(isb);
                        }

                        if (don.equals("2")){
                            System.out.println("\nOk!");
                            System.out.println("Book not Borrowed!");
                        } else if (don.equals("3")){
                            System.out.println("\nBook Borrowed by another user!");
                            System.out.println("Book not Borrowed!");                        
                        } else {
                            System.out.println("\nDone!");
                            System.out.println("Book "+don+" successfully borrowed!");
                            System.out.println("You must return the book in 7 Days!");

                            Book a = new Book();
                            isb = a.mdIsb(isb);

                            PreparedStatement ms = connection.prepareStatement("update books set avail = 0 where isbn = ?");
                            ms.setString(1, isb);
                            ms.executeUpdate();

                            SimpleDateFormat ft = new SimpleDateFormat("dd-MM-yyyy"); 
                            String dat = ft.format(new Date()); 
                            
                            ResultSet resultSetB;

                            PreparedStatement mys2 = connection.prepareStatement("SELECT Title FROM Books where isbn = ?");
                            mys2.setString(1, isb);

                            resultSetB = mys2.executeQuery();
                            resultSetB.next();
                            String tit = resultSetB.getString(1);

                            ResultSet resultSetC;   
                            resultSetC = statement.executeQuery("SELECT count(*) FROM BORROWINGS");
                            resultSetC.next();
                            int idm = resultSetC.getInt(1) + 1;

                            PreparedStatement mys1 = connection.prepareStatement("INSERT into Borrowings (ID, isbn, Title, Reader, IssueDate, ReturnDate, Returned) VALUE (?, ?, ?, ?, ?, ?, ?)");
                            mys1.setInt(1, idm);
                            mys1.setString(2, isb);
                            mys1.setString(3, tit);
                            mys1.setString(4, email);
                            mys1.setString(5, dat);
                            mys1.setString(6, "");
                            mys1.setBoolean(7, false);
                            mys1.executeUpdate();

                        }
                        System.out.println();
                    }
                    else {
                        System.out.println("\nNo Book present in the library!\n");
                    }
                }

                if (com == 4){
                    boolean IsLen = myObj.checkIf();
                    if (IsLen){
                        System.out.println("\nTo return a Book :");
                        System.out.print("Please enter isbn of the desired book : ");
                        String isb = me.nextLine();

                        Book a = new Book();
                        isb = a.mdIsb(isb);

                        ResultSet resultSet7;
                        resultSet7 = statement.executeQuery("SELECT * FROM BORROWINGS");

                        boolean borrowed = false;
                        boolean youBor = false;

                        while(resultSet7.next()){
                            if (resultSet7.getString(2).equals(isb)){
                                borrowed = true;
                                if (resultSet7.getString(4).equals(email)){
                                    youBor = true;
                                }
                            }
                        }

                        if (!(borrowed)){
                            System.out.println("\nBook Not Borrowed by any user!");
                        }

                        else if (!(youBor)){
                            System.out.println("\nBook not Borrowed by you!");
                        }
                        
                        else {
                            String don = myObj.returnBook(isb);
                            while (don.equals("0")){
                                System.out.println("\nBook with ISBN does not exist!\n");

                                System.out.print("Please enter isbn of the book : ");
                                isb = me.nextLine();
                                don = myObj.returnBook(isb);
                            }

                            if (don.equals("2")){
                                System.out.println("\nOk!");
                                System.out.println("Book not returned!");
                            } else if (don.equals("3")){
                                System.out.println("\nBook Not Borrowed by any user!");
                            } else {
                                System.out.println("\nDone!");
                                System.out.println("Book "+don+" successfully returned!");

                                Book ax = new Book();
                                isb = ax.mdIsb(isb);

                                PreparedStatement ms = connection.prepareStatement("update books set avail = 1 where isbn = ?");
                                ms.setString(1, isb);
                                ms.executeUpdate();

                                SimpleDateFormat ft = new SimpleDateFormat("dd-MM-yyyy"); 
                                String dat = ft.format(new Date()); 

                                PreparedStatement msT = connection.prepareStatement("update borrowings set returndate = ? where isbn = ? and returned = ?");         
                                msT.setString(1, dat);
                                msT.setString(2, isb);
                                msT.setInt(3, 0);
                                msT.executeUpdate();

                                ResultSet resA;
                                PreparedStatement msU = connection.prepareStatement("select IssueDate from Borrowings where isbn = ? and returned = ?");         
                                msU.setString(1, isb);
                                msU.setInt(2, 0);
                                resA = msU.executeQuery();

                                resA.next();
                                String datI = resA.getString(1);

                                PreparedStatement msY = connection.prepareStatement("update borrowings set returned = ? where isbn = ? and returned = ?");         
                                msY.setInt(1, 1);
                                msY.setString(2, isb);
                                msY.setInt(3, 0);
                                msY.executeUpdate();

                                SimpleDateFormat fr = new SimpleDateFormat("dd MM yyyy"); 

                                String myDat = "";
                                for (int i = 0; i < datI.length(); i++){
                                    if (!(String.valueOf(datI.charAt(i)).equals("-"))){
                                        myDat = myDat + String.valueOf(datI.charAt(i));
                                    }
                                    else {
                                        myDat = myDat + " ";
                                    }
                                }

                                String datR = fr.format(new Date()); 

                                Date dat1 = fr.parse(myDat);
                                Date dat2 = fr.parse(datR);

                                long diff = dat2.getTime() - dat1.getTime();

                                long day = TimeUnit.DAYS.convert(diff, TimeUnit.MILLISECONDS);
                                System.out.println ("\nDays: " + day);

                                if (day > 7){
                                    int del = (int)day - 7;
                                    int fine = del * 10;


                                    ResultSet resB;
                                    PreparedStatement msV = connection.prepareStatement("select Score from Credentials where email = ?");         
                                    msV.setString(1, email);
                                    resB = msV.executeQuery();
                                    resB.next();
                                    int cs = resB.getInt(1);

                                    cs -= fine;

                                    msV = connection.prepareStatement("update credentials set Score = ? where email = ?");         
                                    msV.setInt(1, cs);
                                    msV.setString(2, email);
                                    msV.executeUpdate();

                                    String sc;
                                    if (cs > 799){
                                        sc = "Excellent";
                                    }
                                    else if (cs >= 650 && cs <= 799){
                                        sc = "Good";
                                    }
                                    else if (cs >= 450 && cs <= 649){
                                        sc = "Fair";
                                    }
                                    else if (cs >= 300 && cs <= 449){
                                        sc = "Poor";
                                    }
                                    else {
                                        sc = "Very Bad";
                                    }
                                    
                                    System.out.println("\nYou are delayed by "+del+" days");
                                    System.out.println("You have a Deduction of "+fine+" Credit Points!");
                                    System.out.println("Now your credit score is "+cs+" and is "+sc+"!");

                                    if (sc == "Very Bad"){
                                        System.out.println("\nAs you Credit score is less than 300!");
                                        System.out.println("Your account is made inactive and you won't be allowed to use the Library!");

                                        msV = connection.prepareStatement("update credentials set Inactive = ? where email = ?");         
                                        msV.setInt(1, 1);
                                        msV.setString(2, email);
                                        msV.executeUpdate();

                                        Ina = false;
                                    }
                                }
                                else if ( day < 7){
                                    int eal = 7 - (int)day;
                                    int bonus = eal * 10;

                                    ResultSet resB;
                                    PreparedStatement msV = connection.prepareStatement("select Score from Credentials where email = ?");         
                                    msV.setString(1, email);
                                    resB = msV.executeQuery();
                                    resB.next();
                                    int cs = resB.getInt(1);

                                    cs += bonus;

                                    msV = connection.prepareStatement("update credentials set Score = ? where email = ?");         
                                    msV.setInt(1, cs);
                                    msV.setString(2, email);
                                    msV.executeUpdate();

                                    String sc;
                                    if (cs > 799){
                                        sc = "Excellent";
                                    }
                                    else if (cs >= 650 && cs <= 799){
                                        sc = "Good";
                                    }
                                    else if (cs >= 450 && cs <= 649){
                                        sc = "Fair";
                                    }
                                    else if (cs >= 300 && cs <= 449){
                                        sc = "Poor";
                                    }
                                    else {
                                        sc = "Very Bad";
                                    }

                                    System.out.println("\nThank You for being On Time!");
                                    System.out.println("You have an Increase of "+bonus+" Credit Points!");
                                    System.out.println("Now your credit score is "+cs+" and is "+sc+"!");
                                }
                                else {
                                    System.out.println("\nThank You for being On Time!");
                                }
                            }
                            System.out.println();
                        }
                    }
                    else {
                        System.out.println("\nNo Book present in the library!\n");
                    }
                }

                if (com == 5){
                    Library myOb = new Library();
                    myOb.dispayBooks();
                    //myOb.displayLib();
                }
                
                if (Ina){
                    System.out.print("Do you want to enter more commands (Y/N) ?");
                    use = me.nextLine();
                    use = use.toUpperCase();

                    while (!(use.equals("Y")) && !(use.equals("N"))){
                        System.out.println("Invalid Input!");
                        System.out.print("\nDo you want to enter more commands (Y/N) ?");
                        use = me.nextLine();
                        use = use.toUpperCase();
                    }
                }
            }    

            System.out.println("Bye! Thanks for using!"); 
            //System.out.print("List containing isbn codes -> ");  
            //System.out.println(listIsb);
            
            statement.close();
            connection.close();
            me.close();
        }
        catch (Exception exception) {
            System.out.println(exception);
        }
    }
}
