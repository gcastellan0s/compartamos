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
        @submit.stop.prevent='getNIP(form)'
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
                placeholder='ej. 9999 - 9999 - 9999 - 9999'
                hint='16 numeros de su tarjeta bancaria'
                :rules="[val => !!val || 'Ingresa un numero de tarjeta', val => val.length === 25 || 'Ingresa un numero válido']"
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
                placeholder='ej .JUAN PEREZ R'
                hint='Número tal como aparece en su tarjeta'
                :rules="[val => !!val || 'Ingresa un nombre']"
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
                :rules="[val => !!val || 'Ingresa una fecha', val => val.length === 7 || 'Ingresa una fecha válida']"
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
                :rules="[val => !!val || 'Ingresa un numero', val => val.length === 14 || 'Ingresa un numero válido']"
              )
          q-card-actions.q-mt-lg.full-width(align='right')
            q-btn.text-weight-bold(
              color='primary'
              size=''
              type='submit'
            ) Solicitar contraseña
            q-space
            q-btn.text-weight-bold(
              color='grey'
              size=''
              type='reset'
              @click='reset'
            ) Cancelar
            q-dialog(v-model='success', persistent='', transition-show='scale', transition-hide='scale')
              q-card.bg-positive.text-white(style='width: 300px')
                q-card-section
                  .text-h6
                    | Éxito!
                q-card-section.q-pt-none
                  | Enviamos un mensaje de texto a tu número de teléfono
                q-card-actions.bg-white.text-positive(align='right')
                  q-btn(flat='', label='OK', @click='reload' )
            q-dialog(v-model='error', persistent='', transition-show='scale', transition-hide='scale')
              q-card.bg-negative.text-white(style='width: 300px')
                q-card-section
                  .text-h6
                    | Ooops!
                q-card-section.q-pt-none
                  | Algo no salió bien, por favor revisa tus datos
                q-card-actions.bg-white.text-negative(align='right')
                  q-btn(flat='', label='OK', v-close-popup='')
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
        numero_movil: '(55) 3723 2182'
      },
      success: false,
      error: false
    }
  },
  methods: {
    validate () {
      if (this.$refs.form.validate()) return 1
      return 0
    },
    getNIP (form) {
      if (!this.validate()) return 0
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
          this.success = true
        })
        .catch(() => {
          this.error = true
        })
    },
    reload () {
      location.reload()
    },
    reset () {
      this.success = false
      this.form = {
        numero_tarjeta: '',
        nombre: '',
        fecha_vencimiento: '',
        fecha_vencimiento_mes: '',
        fecha_vencimiento_ano: '',
        numero_movil: ''
      }
      this.$refs.form.resetValidation()
    }
  }
}
</script>
