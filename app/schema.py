import graphene
from starlette_graphene3 import GraphQLApp
from django.core.cache import cache
import redis
import json
r = redis.Redis(
  #host='redis-14646.c301.ap-south-1-1.ec2.cloud.redislabs.com',
  host="10.80.61.20",
  port=6379,
  decode_responses=True)
customers_data__=[
    {
      "name": "Alice",
      "productName": "Product A",
      "mobileNo": "123-456-7890"
    },
    {
      "name": "Bob",
      "productName": "Product B",
      "mobileNo": "987-654-3210"
    },
    
    {
      "name": "chan",
      "productName": "Product YYY",
      "mobileNo": "987-654-3211"
    },
    {
      "name": "Charlie",
      "productName": "Product C",
      "mobileNo": "111-222-3333"
    },
    {
      "name": "Diana",
      "productName": "Product D",
      "mobileNo": "444-555-6666"
    }
  ]


customers_data = [d for d in json.loads(r.get("test"))]


class CustomersSchema(graphene.ObjectType):
  id=graphene.Int()
  timestamp=graphene.String()
  mac_address=graphene.String()
  model_version=graphene.String()
  dvbs2_lock_status=graphene.Int()
  dvbs2_input_dbm=graphene.Int()
  dvbs2_snr=graphene.Int()
  dvbs2_per=graphene.Float()
  dvbs2_code_rate=graphene.Int()
  dvbs2_modulation=graphene.Int()
  dvbs2_roll_of_factor=graphene.Float()
  dvbs2_tuner_voltage=graphene.Int()
  dvbs2_mpe_section_error_count=graphene.Int()
  dvbs2_rtp_seq_error_count=graphene.Int()
  dvbs2_ts_continuity_error_count=graphene.Int()
  dvbs2_backhaul_misc_error_count=graphene.Int()
  gps_lock_status=graphene.Int()
  gps_epoc_time=graphene.Int()
  gps_latitude=graphene.Float()
  gps_longitude=graphene.Float()
  pipeline_sched_last_proc_latency=graphene.Float()
  pipeline_sched_stl_out_rate=graphene.Int()
  pipeline_sched_emission_rate=graphene.Int()
  pipeline_sched_curr_sampling_rate=graphene.Int()
  pipeline_sched_buffered_jitter_frame_count=graphene.Int()
  subframe0_plp0_active=graphene.Int()
  subframe0_plp0_mod_code=graphene.Int()
  subframe0_plp0_ldpc_len=graphene.Int()
  subframe0_plp0_ldpc_type=graphene.Int()
  subframe0_plp0_code_rate=graphene.Int()
  subframe0_plp0_outer_parity_type=graphene.Int()
  subframe0_plp1_active=graphene.Int()
  subframe0_plp1_mod_code=graphene.Int()
  subframe0_plp1_ldpc_len=graphene.Int()
  subframe0_plp1_ldpc_type=graphene.Int()
  subframe0_plp1_code_rate=graphene.Int()
  subframe0_plp1_outer_parity_type=graphene.Int()
  subframe0_plp2_active=graphene.Int()
  subframe0_plp2_mod_code=graphene.Int()
  subframe0_plp2_ldpc_len=graphene.Int()
  subframe0_plp2_ldpc_type=graphene.Int()
  subframe0_plp2_code_rate=graphene.Int()
  subframe0_plp2_outer_parity_type=graphene.Int()
  subframe0_plp3_active=graphene.Int()
  subframe0_plp3_mod_code=graphene.Int()
  subframe0_plp3_ldpc_len=graphene.Int()
  subframe0_plp3_ldpc_type=graphene.Int()
  subframe0_plp3_code_rate=graphene.Int()
  subframe0_plp3_outer_parity_type=graphene.Int()
  subframe0_active=graphene.Int()
  subframe0_fft_size=graphene.Int()
  subframe0_gi_config=graphene.Int()
  subframe0_pilot_config=graphene.Int()
  subframe1_plp0_active=graphene.Int()
  subframe1_plp0_mod_code=graphene.Int()
  subframe1_plp0_ldpc_len=graphene.Int()
  subframe1_plp0_ldpc_type=graphene.Int()
  subframe1_plp0_code_rate=graphene.Int()
  subframe1_plp0_outer_parity_type=graphene.Int()
  subframe1_plp1_active=graphene.Int()
  subframe1_plp1_mod_code=graphene.Int()
  subframe1_plp1_ldpc_len=graphene.Int()
  subframe1_plp1_ldpc_type=graphene.Int()
  subframe1_plp1_code_rate=graphene.Int()
  subframe1_plp1_outer_parity_type=graphene.Int()
  subframe1_plp2_active=graphene.Int()
  subframe1_plp2_mod_code=graphene.Int()
  subframe1_plp2_ldpc_len=graphene.Int()
  subframe1_plp2_ldpc_type=graphene.Int()
  subframe1_plp2_code_rate=graphene.Int()
  subframe1_plp2_outer_parity_type=graphene.Int()
  subframe1_plp3_active=graphene.Int()
  subframe1_plp3_mod_code=graphene.Int()
  subframe1_plp3_ldpc_len=graphene.Int()
  subframe1_plp3_ldpc_type=graphene.Int()
  subframe1_plp3_code_rate=graphene.Int()
  subframe1_plp3_outer_parity_type=graphene.Int()
  subframe1_active=graphene.Int()
  subframe1_fft_size=graphene.Int()
  subframe1_gi_config=graphene.Int()
  subframe1_pilot_config=graphene.Int()
  system_stats_system_uptime=graphene.Int()
  system_stats_active_running_time=graphene.Int()
  system_stats_brh_bist_status=graphene.Int()
  system_stats_brh_temp=graphene.Float()
  system_stats_brh_last_downtime_start=graphene.Int()
  system_stats_brh_last_downtime_end=graphene.Int()
  bb_board_tx_gain=graphene.Float()
  pa_control=graphene.Int()
  stltp_smpte_columns=graphene.Int()
  stltp_smpte_rows=graphene.Int()
  system_stats_driver_pa_temp=graphene.Float()
  system_stats_fullnim_temp=graphene.Float()
  system_stats_proc_ps_temp=graphene.Float()
  system_stats_pa_ps_temp=graphene.Float()
  system_stats_rfssg_temp=graphene.Float()
  system_stats_som_external_temp=graphene.Float()
  system_stats_som_internal_temp=graphene.Float()
  system_stats_main_pa_temp=graphene.Float()
  system_stats_p3bb_temp=graphene.Float()
  system_stats_pa_50v_current=graphene.Float()
  system_stats_pa_50v_voltage=graphene.Float()
  system_stats_proc_12v_current=graphene.Float()
  system_stats_proc_12v_voltage=graphene.Float()
  system_stats_proc_6v_current=graphene.Float()
  system_stats_proc_6v_voltage=graphene.Float()
  system_stats_rev_pwr_voltage=graphene.Float()
  system_stats_fwd_pwr_voltage=graphene.Float()
  system_stats_vga_value=graphene.Float()
  system_stats_placeholder1=graphene.Float()
  system_stats_placeholder2=graphene.Float()
  system_stats_placeholder3=graphene.Float()
  system_stats_placeholder4=graphene.Float()
  system_stats_placeholder5=graphene.Float()
class Query(graphene.ObjectType):
    
    filter=graphene.Field(CustomersSchema,mac_address=graphene.String())
    filter_all_data=graphene.List(CustomersSchema)
    def resolve_filter_all_data(self,info):

      return customers_data
    
    def resolve_filter(self,info,mac_address):
      #print(id)
      for cust_data in customers_data:
        #print(cust_data)
        if mac_address==cust_data['mac_address']:
          #print('hi')
          return cust_data
        else:
          #print('byee')
          return{
      "name": None,
      "productName": None,
      "mobileNo": None
    }
    
    
schema = graphene.Schema(query=Query)