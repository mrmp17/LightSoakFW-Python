from peewee import *

database_proxy = Proxy() # Create a proxy for our db.

class LightSoakDatabase:
    def __init__(self, out_dir):
        self.__out_dir = out_dir


    def open_db(self):
        self.db = SqliteDatabase(self.__out_dir + "lightSoakDB.db")
        database_proxy.initialize(self.db)
        self.__create_tables()

    def __create_tables(self):
        with self.db:
            self.db.create_tables([Measurement, BufferDump, CharacteristicIV])

    def save_to_db(self, data_dict):
        if(data_dict["type"] == "getvolt"):
            self.__save_getvolt(data_dict)
            
        elif(data_dict["type"] == "getcurr"):
            self.__save_getcurr(data_dict)

        elif(data_dict["type"] == "getivpoint"):
            self.__save_getivpoint(data_dict)

        elif(data_dict["type"] == "flashmeasure_dumpvolt"):
            self.__save_flashmeasure_dumpvolt(data_dict)

        elif(data_dict["type"] == "flashmeasure_dumpcurr"):
            self.__save_flashmeasure_dumpcurr(data_dict)

        elif(data_dict["type"] == "dumpvolt"):
            self.__save_dumpvolt(data_dict)

        elif(data_dict["type"] == "dumpcurr"):
            self.__save_dumpcurr(data_dict)

        elif(data_dict["type"] == "dumpiv"):
            self.__save_dumpiv(data_dict)

        elif(data_dict["type"] == "getivchar"):
            self.__save_getivchar(data_dict)
        
        elif(data_dict["type"] == "getledtemp"):
            self.__save_getledtemp(data_dict)



    def close_db(self):
        self.db.close()

    def __save_getvolt(self, data_dict):
        meas = Measurement(
            timestamp = data_dict.get("timestamp", None),
            ch1 = data_dict.get("ch1", None),
            ch2 = data_dict.get("ch2", None),
            ch3 = data_dict.get("ch3", None),
            ch4 = data_dict.get("ch4", None),
            ch5 = data_dict.get("ch5", None),
            ch6 = data_dict.get("ch6", None),
            DUT_temp = data_dict.get("DUT_temp", None),
            meas_type = data_dict.get("type")
        )
        meas.save()

    def __save_getcurr(self, data_dict):
        meas = Measurement(
            timestamp = data_dict.get("timestamp", None),
            ch1_curr = data_dict.get("ch1_curr", None),
            ch2_curr = data_dict.get("ch2_curr", None),
            ch3_curr = data_dict.get("ch3_curr", None),
            ch4_curr = data_dict.get("ch4_curr", None),
            ch5_curr = data_dict.get("ch5_curr", None),
            ch6_curr = data_dict.get("ch6_curr", None),
            DUT_temp = data_dict.get("DUT_temp", None),
            meas_type = data_dict.get("type")
        )
        meas.save()

    def __save_getivpoint(self, data_dict):
        meas = Measurement(
            timestamp = data_dict.get("timestamp", None),
            ch1 = data_dict.get("ch1", None),
            ch2 = data_dict.get("ch2", None),
            ch3 = data_dict.get("ch3", None),
            ch4 = data_dict.get("ch4", None),
            ch5 = data_dict.get("ch5", None),
            ch6 = data_dict.get("ch6", None),
            ch1_curr = data_dict.get("ch1_curr", None),
            ch2_curr = data_dict.get("ch2_curr", None),
            ch3_curr = data_dict.get("ch3_curr", None),
            ch4_curr = data_dict.get("ch4_curr", None),
            ch5_curr = data_dict.get("ch5_curr", None),
            ch6_curr = data_dict.get("ch6_curr", None),
            DUT_temp = data_dict.get("DUT_temp", None),
            meas_type = data_dict.get("type"),
            # for testing
            ledtemp = data_dict.get("ledtemp", None)
        )
        meas.save()


    def __save_dumpvolt(self, data_dict):
        meas = Measurement(
            timestamp = data_dict.get("timestamp", None),
            # todo: implement getting voltage from bufferfump if needed
            ch1 = None,
            ch2 = None,
            ch3 = None,
            ch4 = None,
            ch5 = None,
            ch6 = None,
            DUT_temp = data_dict.get("DUT_temp", None),
            meas_type = data_dict.get("type"),
            sample_count = data_dict.get("sample_count")
        )
        meas.save()
        #no save bufferdump for this measurement
        self.__save_dumpvolt_to_bufferdump(data_dict, meas)

    def __save_dumpiv(self, data_dict):
        meas = Measurement(
            timestamp = data_dict.get("timestamp", None),
            # todo: implement getting voltage from bufferfump if needed
            ch1 = None,
            ch2 = None,
            ch3 = None,
            ch4 = None,
            ch5 = None,
            ch6 = None,
            ch1_curr = None,
            ch2_curr = None,
            ch3_curr = None,
            ch4_curr = None,
            ch5_curr = None,
            ch6_curr = None,
            DUT_temp = data_dict.get("DUT_temp", None),
            meas_type = data_dict.get("type"),
            sample_count = data_dict.get("sample_count")
        )
        meas.save()
        #no save bufferdump for this measurement
        self.__save_dumpiv_to_bufferdump(data_dict, meas)

    def __save_dumpcurr(self, data_dict):
        meas = Measurement(
            timestamp = data_dict.get("timestamp", None),
            # todo: implement getting voltage from bufferfump if needed
            ch1_curr = None,
            ch2_curr = None,
            ch3_curr = None,
            ch4_curr = None,
            ch5_curr = None,
            ch6_curr = None,
            DUT_temp = data_dict.get("DUT_temp", None),
            meas_type = data_dict.get("type"),
            sample_count = data_dict.get("sample_count")
        )
        meas.save()
        #no save bufferdump for this measurement
        self.__save_dumpcurr_to_bufferdump(data_dict, meas)


    def __save_flashmeasure_dumpvolt(self, data_dict):
        meas = Measurement(
            timestamp = data_dict.get("timestamp", None),
            # todo: implement getting voltage from bufferfump if needed
            ch1 = data_dict.get("ch1", None),
            ch2 = data_dict.get("ch2", None),
            ch3 = data_dict.get("ch3", None),
            ch4 = data_dict.get("ch4", None),
            ch5 = data_dict.get("ch5", None),
            ch6 = data_dict.get("ch6", None),
            DUT_temp = data_dict.get("DUT_temp", None),
            meas_type = data_dict.get("type"),
            sample_count = data_dict.get("sample_count")
        )
        meas.save()
        #no save bufferdump for this measurement
        self.__save_dumpvolt_to_bufferdump(data_dict, meas)

    def __save_flashmeasure_dumpcurr(self, data_dict):
        meas = Measurement(
            timestamp = data_dict.get("timestamp", None),
            # todo: implement getting voltage from bufferfump if needed
            ch1_curr = None,
            ch2_curr = None,
            ch3_curr = None,
            ch4_curr = None,
            ch5_curr = None,
            ch6_curr = None,
            DUT_temp = data_dict.get("DUT_temp", None),
            meas_type = data_dict.get("type"),
            sample_count = data_dict.get("sample_count")
        )
        meas.save()
        #no save bufferdump for this measurement
        self.__save_dumpcurr_to_bufferdump(data_dict, meas)


    def __save_dumpvolt_to_bufferdump(self, data_dict, measurement_id):
        for _ in range(data_dict.get("sample_count")):
            if "CH1_samples" in data_dict:
                (t1, s1) = data_dict["CH1_samples"].pop(0)
            else:
                (t1, s1) = (None, None)
            if "CH2_samples" in data_dict:
                (t2, s2) = data_dict["CH2_samples"].pop(0)
            else:
                (t2, s2) = (None, None)
            if "CH3_samples" in data_dict:
                (t3, s3) = data_dict["CH3_samples"].pop(0)
            else:
                (t3, s3) = (None, None)
            if "CH4_samples" in data_dict:
                (t4, s4) = data_dict["CH4_samples"].pop(0)
            else:
                (t4, s4) = (None, None)
            if "CH5_samples" in data_dict:
                (t5, s5) = data_dict["CH5_samples"].pop(0)
            else:
                (t5, s5) = (None, None)
            if "CH6_samples" in data_dict:
                (t6, s6) = data_dict["CH6_samples"].pop(0)
            else:
                (t6, s6) = (None, None)

            # gets timestamp of sample from first present channel
            ts = [t1, t2, t3, t4, t5, t6]
            for a in ts:
                if a is not None:
                    t = a

        
            bufdump = BufferDump(
                timestamp = t,
                ch1 = s1,
                ch2 = s2,
                ch3 = s3,
                ch4 = s4,
                ch5 = s5,
                ch6 = s6,
                measurement = measurement_id
            )
            bufdump.save()
        pass

    def __save_dumpcurr_to_bufferdump(self, data_dict, measurement_id):
        for _ in range(data_dict.get("sample_count")):
            if "CH1_curr_samples" in data_dict:
                (t1, s1) = data_dict["CH1_curr_samples"].pop(0)
            else:
                (t1, s1) = (None, None)
            if "CH2_curr_samples" in data_dict:
                (t2, s2) = data_dict["CH2_curr_samples"].pop(0)
            else:
                (t2, s2) = (None, None)
            if "CH3_curr_samples" in data_dict:
                (t3, s3) = data_dict["CH3_curr_samples"].pop(0)
            else:
                (t3, s3) = (None, None)
            if "CH4_curr_samples" in data_dict:
                (t4, s4) = data_dict["CH4_curr_samples"].pop(0)
            else:
                (t4, s4) = (None, None)
            if "CH5_curr_samples" in data_dict:
                (t5, s5) = data_dict["CH5_curr_samples"].pop(0)
            else:
                (t5, s5) = (None, None)
            if "CH6_curr_samples" in data_dict:
                (t6, s6) = data_dict["CH6_curr_samples"].pop(0)
            else:
                (t6, s6) = (None, None)

            # gets timestamp of sample from first present channel
            ts = [t1, t2, t3, t4, t5, t6]
            for a in ts:
                if a is not None:
                    t = a

        
            bufdump = BufferDump(
                timestamp = t,
                ch1_curr = s1,
                ch2_curr = s2,
                ch3_curr = s3,
                ch4_curr = s4,
                ch5_curr = s5,
                ch6_curr = s6,
                measurement = measurement_id
            )
            bufdump.save()
        pass

    def __save_dumpiv_to_bufferdump(self, data_dict, measurement_id):
        # todo: implementation not very elegant, but works
        for _ in range(data_dict.get("sample_count")):
            if "CH1_samples" in data_dict:
                (t1, s1) = data_dict["CH1_samples"].pop(0)
                (ti1, i1) = data_dict["CH1_curr_samples"].pop(0)
            else:
                (t1, s1) = (None, None)
                i1 = None
            if "CH2_samples" in data_dict:
                (t2, s2) = data_dict["CH2_samples"].pop(0)
                (ti2, i2) = data_dict["CH2_curr_samples"].pop(0)
            else:
                (t2, s2) = (None, None)
                i2 = None
            if "CH3_samples" in data_dict:
                (t3, s3) = data_dict["CH3_samples"].pop(0)
                (ti3, i3) = data_dict["CH3_curr_samples"].pop(0)
            else:
                (t3, s3) = (None, None)
                i3 = None
            if "CH4_samples" in data_dict:
                (t4, s4) = data_dict["CH4_samples"].pop(0)
                (ti4, i4) = data_dict["CH4_curr_samples"].pop(0)
            else:
                (t4, s4) = (None, None)
                i4 = None
            if "CH5_samples" in data_dict:
                (t5, s5) = data_dict["CH5_samples"].pop(0)
                (ti5, i5) = data_dict["CH5_curr_samples"].pop(0)
            else:
                (t5, s5) = (None, None)
                i5 = None
            if "CH6_samples" in data_dict:
                (t6, s6) = data_dict["CH6_samples"].pop(0)
                (ti6, i6) = data_dict["CH6_curr_samples"].pop(0)
            else:
                (t6, s6) = (None, None)
                i6 = None

            # gets timestamp of sample from first present channel
            ts = [t1, t2, t3, t4, t5, t6]
            for a in ts:
                if a is not None:
                    t = a

        
            bufdump = BufferDump(
                timestamp = t,
                ch1 = s1,
                ch2 = s2,
                ch3 = s3,
                ch4 = s4,
                ch5 = s5,
                ch6 = s6,
                ch1_curr = i1,
                ch2_curr = i2,
                ch3_curr = i3,
                ch4_curr = i4,
                ch5_curr = i5,
                ch6_curr = i6,
                measurement = measurement_id
            )
            bufdump.save()
        pass

    def __save_getivchar(self, data_dict):
        meas = Measurement(
            timestamp = data_dict.get("timestamp", None),
            # todo: implement getting voltage from bufferfump if needed
            ch1 = None,
            ch2 = None,
            ch3 = None,
            ch4 = None,
            ch5 = None,
            ch6 = None,
            ch1_curr = None,
            ch2_curr = None,
            ch3_curr = None,
            ch4_curr = None,
            ch5_curr = None,
            ch6_curr = None,
            DUT_temp = data_dict.get("DUT_temp", None),
            meas_type = data_dict.get("type"),
            sample_count = data_dict.get("sample_count")
        )
        meas.save()
        #no save bufferdump for this measurement
        self.__save_getivchar_to_bufferdump(data_dict, meas)

    def __save_getivchar_to_bufferdump(self, data_dict, measurement_id):
         # todo: implementation not very elegant, but works
        for _ in range(data_dict.get("sample_count")):
            if "CH1_samples" in data_dict:
                (t1, s1) = data_dict["CH1_samples"].pop(0)
                (ti1, i1) = data_dict["CH1_curr_samples"].pop(0)
            else:
                (t1, s1) = (None, None)
                i1 = None
            if "CH2_samples" in data_dict:
                (t2, s2) = data_dict["CH2_samples"].pop(0)
                (ti2, i2) = data_dict["CH2_curr_samples"].pop(0)
            else:
                (t2, s2) = (None, None)
                i2 = None
            if "CH3_samples" in data_dict:
                (t3, s3) = data_dict["CH3_samples"].pop(0)
                (ti3, i3) = data_dict["CH3_curr_samples"].pop(0)
            else:
                (t3, s3) = (None, None)
                i3 = None
            if "CH4_samples" in data_dict:
                (t4, s4) = data_dict["CH4_samples"].pop(0)
                (ti4, i4) = data_dict["CH4_curr_samples"].pop(0)
            else:
                (t4, s4) = (None, None)
                i4 = None
            if "CH5_samples" in data_dict:
                (t5, s5) = data_dict["CH5_samples"].pop(0)
                (ti5, i5) = data_dict["CH5_curr_samples"].pop(0)
            else:
                (t5, s5) = (None, None)
                i5 = None
            if "CH6_samples" in data_dict:
                (t6, s6) = data_dict["CH6_samples"].pop(0)
                (ti6, i6) = data_dict["CH6_curr_samples"].pop(0)
            else:
                (t6, s6) = (None, None)
                i6 = None

            # gets timestamp of sample from first present channel
            ts = [t1, t2, t3, t4, t5, t6]
            for a in ts:
                if a is not None:
                    t = a

        
            chariv = CharacteristicIV(
                timestamp = t,
                ch1 = s1,
                ch2 = s2,
                ch3 = s3,
                ch4 = s4,
                ch5 = s5,
                ch6 = s6,
                ch1_curr = i1,
                ch2_curr = i2,
                ch3_curr = i3,
                ch4_curr = i4,
                ch5_curr = i5,
                ch6_curr = i6,
                measurement = measurement_id
            )
            chariv.save()
        pass

    def __save_getledtemp(self, data_dict):
        meas = Measurement(
            timestamp = data_dict.get("timestamp", None),
            DUT_temp = data_dict.get("DUT_temp", None),
            meas_type = data_dict.get("type"),
            ledtemp = data_dict.get("ledtemp", None),
        )
        meas.save()
            





# database model classes

class BaseModel(Model):
    class Meta:
        database = database_proxy


class Measurement(BaseModel):
    timestamp = IntegerField()
    ch1 = FloatField(null=True)
    ch2 = FloatField(null=True)
    ch3 = FloatField(null=True)
    ch4 = FloatField(null=True)
    ch5 = FloatField(null=True)
    ch6 = FloatField(null=True)
    ch1_curr = FloatField(null=True)
    ch2_curr = FloatField(null=True)
    ch3_curr = FloatField(null=True)
    ch4_curr = FloatField(null=True)
    ch5_curr = FloatField(null=True)
    ch6_curr = FloatField(null=True)
    DUT_temp = FloatField()
    ledtemp = FloatField(null=True)
    meas_type = TextField()
    sample_count = IntegerField(null=True)

class BufferDump(BaseModel):
    timestamp = IntegerField()
    ch1 = FloatField(null=True)
    ch2 = FloatField(null=True)
    ch3 = FloatField(null=True)
    ch4 = FloatField(null=True)
    ch5 = FloatField(null=True)
    ch6 = FloatField(null=True)
    ch1_curr = FloatField(null=True)
    ch2_curr = FloatField(null=True)
    ch3_curr = FloatField(null=True)
    ch4_curr = FloatField(null=True)
    ch5_curr = FloatField(null=True)
    ch6_curr = FloatField(null=True)
    #reference to row from Measurement table
    measurement = ForeignKeyField(Measurement, backref='buffer_dump')

class CharacteristicIV(BaseModel):
    timestamp = IntegerField()
    ch1 = FloatField(null=True)
    ch2 = FloatField(null=True)
    ch3 = FloatField(null=True)
    ch4 = FloatField(null=True)
    ch5 = FloatField(null=True)
    ch6 = FloatField(null=True)
    ch1_curr = FloatField(null=True)
    ch2_curr = FloatField(null=True)
    ch3_curr = FloatField(null=True)
    ch4_curr = FloatField(null=True)
    ch5_curr = FloatField(null=True)
    ch6_curr = FloatField(null=True)
    #reference to row from Measurement table
    measurement = ForeignKeyField(Measurement, backref='characteristic_iv')



