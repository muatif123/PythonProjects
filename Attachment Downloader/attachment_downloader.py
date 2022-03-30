# Importing the required library 
import ezgmail


# Defining the function for the downloading the attachment
def attachmentDownload(resultthreads):
    
    # GmailThreads and GamilMessage objects are used:
        # GmailThreads : Represents conversation threads
        # GmailMessage : Represents individual emails within threads

    resultCount = len(resultthreads)
    try:
        for i in range(resultCount):
            # to check whether the count of messages in threads is greater than 1
            if len(resultthreads[i].messages) > 1:
                for j in range(len(resultthreads[i].messages)):
                    resultthreads[i].messages[j].downloadAllAttachments()   # Downloads all the attachments of the email
            else:
                resultthreads[i].messages[0].downloadAllAttachments()    # Downloads the single attachment of the email
        print('Download Completed.')
    except:
        raise Exception("Error occured while downloading the attachment(s).")

    if __name__ == '__main__':
        query = input('Enter seach query: ')
        newquery  = query + " + has:attachment"     # Appending to make sure the result thread always has an attachment
        resultthreads = ezgmail.search(newquery)     # Search functions accepts all the operators described at google support mail

        if len(resultthreads) == 0:
            print('Result has no attachment')
        else:
            print('Result has attachment(s)')
            for threads in resultthreads:
                print(f"Email Subject: {threads.meesages[0].subject}")      # Prints out the subject line thread in results

            try:
                ask = input("Do you want to download the attachmemt(s) in result(s) ? (Yes/No) ")       # Let the user decide whether they want to download the attachment
                if ask == 'Yes':
                    attachmentDownload(resultthreads)       # Call the function to download the attachment
                else:
                    print('Program exited')
            except:
                print('Oops..! Something went wrong.')

        