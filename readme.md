# Indala Weigand Converter
<br />
<br />
Through trial and error, I discovered that the Weigand value read from an Indala RFID card is not the same value that needs to be written to a new card to create a cloned copy. The bits are in a scrambled, but predictable order. This script converts the "Wiegand" hex value recorded by an Indala RFID reader into the correct hex value to be written to an Indala card (via Proxmark) to create a copy. 
<br />
<br />
Example:

~~~~
myhost$ ./indala.py 2005b8272e

Converting Wiegand hex value 2005b8272e to Indala format...
Wiegand 26 bit binary value: 01101110000010011100101110
Checksum ( 5 ) is odd. Adding '01' to bytes 30 and 31.

--Candidate 1 (Try this one first)--
Indala binary value: 0b10010000110000111111011001010001101
Indala hex value to write to card: 4861fb28d

--Candidate 2 (This will probably also work)--
Indala binary value: 0b10010000110000111111011001010010101
Indala hex value to write to card: 4861fb295

Alternate Indala values to try if the above values do not work (these are only used in rare Indala configurations):
4861fb295
4861fb29d

myhost$
~~~~

Although the script creates 4 values, the first one ("Candidate 1") has worked in my real-world testing 100% of the time. The other values are really just included in case I run into something unusual.

To write a cloned copy card with the Proxmark software (using the above example), you would use this command: 
~~~~
lf indalaclone 4861fb28d
~~~~
