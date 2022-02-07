# Encryption,Compression and Hashing

Compression is used to reduce the size of a file. Compression is required to save bandwidth on networks allowing the data to travel quicker and increase HDD space.There are two types of compression Lossless and Lossy compression.Lossless compression is when a file is compressed without the loss of data this is usually done on text files and simple images as data can not be lost in text files,Data will be stored so that the files can be reconstructed fully when the data has been received.Lossy compression on the other hand is when data is discarded in order to reduce files size this usually takes place on videos,audio and complicated images.The data discarded will be the most irrelevant data within the file for example audio files will have their higher frequencies removed that can not be heard by the human ear.
Just like compression there are two types of lossless compression dictionary coding and run length encoding. Dictionary coding is used when lossless compression is being used to reduce the size of a text file it will assign values to the characters within the files so that the file can be reconstructed once received.Run Length Encoding is used to apply lossless compression on simple images with blocks of repeated colour it will store a representation of the pattern of colours e.g 26W 8B 12W.

# Encryption

Since the beginning of language dialect encryption has been around.Encryption is when an original piece of data/messages is scrambled so that it can not be read without the algorithm that has been used to encrypt it. Computer encryption works a  similar way however these algorithms are called encryption keys.

There are two main ways that data is encrypted Asymmetrical and symmetrical encryption. Symmetric encryption is when one key can be used to decrypt and encrypt data this is not secure as the key will have to be obtained by the recipient of the encrypted data which gives hackers a chance to capture the key and create a copy of the key.

 
Asymmetric encryption is much more secure it requires two keys like Symmetrical encryption however these keys are different one is an encrypt key whale the other is an decryption key.The encryption key will be made public allowing somebody to encrypt data and send it to the user with a private decryption key the recipient can have a public key of the sender allowing them to send data to the sender.This limits the possibility of a hacker decrypting the messages as the public key if captured cna only encrypt data tube recipient will also know the origin of the message as they will know who has the private key stopping a hacker mimicking a user. Combining a private key and someone's public key is known as a combined encryption key.

# Hashing

Hashing is the act of irreversibly encrypting data.There are many algorithms that do this one of the most popular being SHA 2 these algorithms are only one way if one character is changed the entire output will be different and if the output is fed through the algorithm it will not return the original message making hashing very secure. Why do this?
Hashing can be used in databases so that plaintext does not have to be transferred giving hackers chance to intercept the data rather it can just go through the algorithm then checked against the data stored within the database.Hashing can also be used for quick memory transfer as data can be encrypted to a simpler form taking up less storage space and ultimately increasing memory speeds.

#Database Charecteristics
Data has been stored and organised long before the existence of computers.Data can be stored on a computer as a database this data is organised so that the data is accessible allowing quick retrieval and writing of data.

Digital databases consist of tables,records and fields these can be thought of as tables,rows and columns.A file holding a single table is referred to as a flat file database and is usually stored as a CSV file they are easy to manage and quick to access however due to the simplicity of these databases there may be duplicate data making the database slow to access and confusing to read.

In order to rectify this, databases can be more complex, linking multiple tables together in order to split up the repeated data and create new tables with a different primary key linking to the original table.

Almost forgot! Tables  and databases consist of keys.Each table will have a primary key(A unique identifier to identify the entity),a secondary key(an index of the primary keys within the database),a Foreign key(A attribute joining the two tables together) and a composite key(A primary key consisting of more than one attribute).

Relationships between tables are similar to ratios, there are only three! 
One to many relationships 1,500
Many to many relationships 500,600
One to one relationships 1,1 

Attribute = Characteristic

