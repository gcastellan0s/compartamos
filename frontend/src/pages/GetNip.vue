<template lang='pug'>
  q-page.flex.flex-center
    q-card.q-card-bordered.shadow-12.q-px-md.q-py-lg(
      style='border-radius: 20px'
      v-bind:style='$q.screen.lt.sm ? {"width": "90%"} : {"width":"40%"}'
    )
      q-card-section
        .text-h6.text-center(
        ) SOLICITUD DE NIP
      q-form(
        ref='form'
        lazy-validation
        @submit.stop.prevent='login'
      )
        q-card-section.q-pa-sm.row
          q-item.col-lg-4.col-md-4.col-sm-12.col-xs-12
            q-item-section.text-right.text-weight-bold(
            ) Número de tarjeta
          q-item.col-lg-8.col-md-8.col-sm-12.col-xs-12
            q-item-section
              q-input(
                v-model='form.numero_tarjeta'
                type='text'
                dense=''
                outlined=''
                round=''
                mask='#### - #### - #### - ####'
                placeholder='9999 - 9999 - 9999 - 9999'
                hint='16 numeros de su tarjeta bancaria'
              )
          q-item.col-lg-4.col-md-4.col-sm-12.col-xs-12
            q-item-section.text-right.text-weight-bold(
            ) Nombre del titular
          q-item.col-lg-8.col-md-8.col-sm-12.col-xs-12
            q-item-section
              q-input(
                v-model='form.nombre'
                type='text'
                dense=''
                outlined=''
                round=''
                placeholder='JUAN PEREZ R'
                hint='Número tal como aparece en su tarjeta'
              )
          q-item.col-lg-4.col-md-4.col-sm-12.col-xs-12
            q-item-section.text-right.text-weight-bold(
            ) Fecha de vecimiento
          q-item.col-lg-8.col-md-8.col-sm-12.col-xs-12
            q-item-section
              q-input(
                v-model='form.fecha_vencimiento'
                type='text'
                dense=''
                outlined=''
                round=''
                mask='##/####'
                placeholder='MM/AAAA'
                hint='Mes a 2 digitos / Año a 4 digitos'
                style='max-width:250px'
              )
          q-separator.q-my-md
          q-item.col-lg-4.col-md-4.col-sm-12.col-xs-12
            q-item-section.text-right.text-weight-bold(
            ) Número móvil
          q-item.col-lg-8.col-md-8.col-sm-12.col-xs-12
            q-item-section
              q-input(
                v-model='form.numero_movil'
                type='text'
                dense=''
                outlined=''
                round=''
                mask='(##) #### ####'
                placeholder='10 dígitos 55-5555-6666'
                hint='Número al que se enviará el NIP'
              )
          q-card-actions.q-mt-lg.full-width(align='right')
            q-btn.text-weight-bold(
              color='primary'
              size=''
              @click='getNIP(form)'
            ) Solicitar contraseña
            q-space
            q-btn.text-weight-bold(
              color='grey'
              size=''
              @click='reset'
            ) Cancelar
</template>

<script>
import { GETNIP } from '@/models/api.js'
export default {
  name: 'GetNip',
  data () {
    return {
      form: {
        numero_tarjeta: '4316 - 1661 - 1223 - 4820',
        nombre: 'ALMA PEREZ A',
        fecha_vencimiento: '08/2021',
        fecha_vencimiento_mes: '',
        fecha_vencimiento_ano: '',
        numero_movil: ''
      }
    }
  },
  methods: {
    getNIP (form) {
      this.$axios
        .get(GETNIP, {
          params: {
            numero_tarjeta: form.numero_tarjeta.replaceAll(' ', '').replaceAll('-', ''),
            nombre: form.nombre,
            fecha_vencimiento_mes: form.fecha_vencimiento.split('/')[0],
            fecha_vencimiento_ano: form.fecha_vencimiento.split('/')[1],
            numero_movil: form.numero_movil.replaceAll(' ', '').replaceAll('(', '').replaceAll(')', '')
          }
        })
        .then(({ data }) => {
          console.log(data)
        })
    },
    reset () {
      this.form = {
        numero_tarjeta: '',
        nombre: '',
        fecha_vencimiento: '',
        fecha_vencimiento_mes: '',
        fecha_vencimiento_ano: '',
        numero_movil: ''
      }
    }
  }
}
</script>
