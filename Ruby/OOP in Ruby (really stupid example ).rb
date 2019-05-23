#showing off BEGIN and END statement
BEGIN{
    puts "starting program"
}
class Contact
    #example of creating a class and class var, also initializing some other vars
    @@no_of_contacts = 0 #class var
    def initialize (email, phone, name)
        @contact_email = email #instance var
        @contact_phone = phone
        @contact_name = name
    end

    def display_info ()
        puts "email is #@contact_email" #similiar to .format in python
        puts "phone number is #@contact_phone"
        puts "name is #@contact_phone"
    end
end

new_contact = Contact.new("evan@srnd.org", "925-542-4419", "Evan Nishi")
new_contact.display_info()

END{
    puts "ending program"
}
